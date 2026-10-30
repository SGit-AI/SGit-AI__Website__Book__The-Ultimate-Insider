// The synthetic readers' runner: each fictional persona opens its review page in a real browser
// (Chromium, with the persona's device) and the runner records what it measured. It writes
// observations.json and three screenshots (a fourth when the pen opens); the review in the persona's voice is written from them.
//
//   node review/synthetic/run.mjs --persona ciso|all [--path /review/<persona>/] [--run <id>] [--out <dir>]
//
// Reads the built site (_site/) from its own local server. Every request to another host is
// blocked and listed: a run sends nothing anywhere (no telemetry). A synthetic reader is a test
// instrument, never a reader.

import { createServer } from 'node:http';
import { readFile, mkdir, writeFile, stat } from 'node:fs/promises';
import { join, extname, normalize, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium, devices } = require('playwright');

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..', '..');
const site = join(root, '_site');

const args = Object.fromEntries(process.argv.slice(2).reduce((acc, a, i, all) =>
  a.startsWith('--') ? [...acc, [a.slice(2), all[i + 1] && !all[i + 1].startsWith('--') ? all[i + 1] : true]] : acc, []));

const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.pdf': 'application/pdf',
  '.woff2': 'font/woff2', '.txt': 'text/plain; charset=utf-8', '.md': 'text/plain; charset=utf-8' };

function serve() {
  const server = createServer(async (req, res) => {
    let path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^(\.\.[/\\])+/, '');
    let file = join(site, path);
    try { if ((await stat(file)).isDirectory()) file = join(file, 'index.html'); } catch {}
    try {
      const body = await readFile(file);
      res.writeHead(200, { 'content-type': TYPES[extname(file)] || 'application/octet-stream' });
      res.end(body);
    } catch { res.writeHead(404); res.end('not found'); }
  });
  return new Promise(ok => server.listen(0, '127.0.0.1', () => ok(server)));
}

async function runOne(browser, base, persona, runId) {
  const device = { ...devices[persona.device.playwright] };
  if (persona.device.viewport) device.viewport = persona.device.viewport;
  delete device.defaultBrowserType;
  const context = await browser.newContext(device);
  const page = await context.newPage();
  const blocked = [], consoleErrors = [], failed = [];
  await page.route('**/*', route => {
    const u = new URL(route.request().url());
    if (u.hostname === '127.0.0.1') return route.continue();
    blocked.push(route.request().url()); return route.abort();
  });
  page.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
  page.on('requestfailed', r => { if (new URL(r.url()).hostname === '127.0.0.1') failed.push(r.url()); });

  const path = args.path || `/review/${persona.id}/`;
  const token = `fictional-${persona.id}-${runId}`;
  const url = `${base}${path}#t=${token}`;
  const out = args.out || join(here, persona.id, runId);
  await mkdir(out, { recursive: true });

  const t0 = Date.now();
  const resp = await page.goto(url, { waitUntil: 'load' }).catch(e => ({ status: () => 0, error: String(e) }));
  const loadMs = Date.now() - t0;
  const status = resp.status();

  const m = await page.evaluate(() => {
    const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
    const paras = [...document.querySelectorAll('main p, article p, p')].filter(vis);
    const uniq = [...new Set(paras)];
    const anchored = uniq.filter(p => p.id || p.closest('[data-a],[data-anchor]'));
    const firstScreen = (document.body.innerText || '').slice(0, 1200);
    const words = (document.body.innerText || '').split(/\s+/).filter(Boolean).length;
    const sizes = uniq.map(p => parseFloat(getComputedStyle(p).fontSize)).filter(Boolean);
    const widths = uniq.slice(0, 40).map(p => {
      const cs = getComputedStyle(p); const ch = parseFloat(cs.fontSize) * 0.5;
      return Math.round(p.getBoundingClientRect().width / ch);
    });
    const links = [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href'));
    return {
      title: document.title,
      h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim()),
      words,
      paragraphs: uniq.length,
      paragraphs_with_own_id: uniq.filter(p => p.id).length,
      paragraphs_inside_an_anchor: anchored.length,
      anchored_blocks: document.querySelectorAll('[data-a]').length,
      questions: document.querySelectorAll('textarea[data-q]').length,
      min_font_px: sizes.length ? Math.min(...sizes) : null,
      median_line_chars_estimate: widths.length ? widths.sort((a, b) => a - b)[Math.floor(widths.length / 2)] : null,
      horizontal_overflow_px: Math.max(0, document.documentElement.scrollWidth - window.innerWidth),
      page_height_screens: Math.round(document.documentElement.scrollHeight / window.innerHeight * 10) / 10,
      links: links.length,
      external_links: links.filter(h => /^https?:/.test(h)).length,
      forms: document.querySelectorAll('form, textarea, [contenteditable]').length,
      fragment_seen_by_page: location.hash.length > 1,
      first_screen_text: firstScreen,
    };
  });

  await page.screenshot({ path: join(out, '1-first-screen.jpg'), type: 'jpeg', quality: 60 });
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight / 2));
  await page.screenshot({ path: join(out, '2-middle.jpg'), type: 'jpeg', quality: 60 });
  await page.evaluate(() => window.scrollTo(0, document.documentElement.scrollHeight));
  await page.screenshot({ path: join(out, '3-end.jpg'), type: 'jpeg', quality: 60 });

  // the pen: one click on the first paragraph, and whether anything appears to comment with
  const PEN = 'dialog[open], [role=dialog], .rv-bar, textarea:not([data-q])';
  const beforeDialogs = await page.locator(PEN).count();
  const anchoredFirst = page.locator('[data-a]').first();   // an anchored block if the page has them, else any paragraph
  const firstPara = (await anchoredFirst.count()) ? anchoredFirst : page.locator('main p, article p').first();
  let pen = 'no paragraph to click', penError = null;
  if (await firstPara.count()) {
    await firstPara.click({ timeout: 3000 }).catch(e => { penError = String(e).split('\n')[0]; });
    await page.waitForTimeout(400);   // the pen is a deferred script: give it a moment to draw
    const after = await page.locator(PEN).count();
    if (after > beforeDialogs) await page.screenshot({ path: join(out, '4-pen.jpg'), type: 'jpeg', quality: 60 });
    pen = after > beforeDialogs ? 'a comment control appeared' : 'nothing appeared';
  }

  const record = {
    schema: 'the-ultimate-insider/synthetic-observations/v1',
    label: 'SYNTHETIC READER: a test instrument, never a reader',
    persona: persona.id, run: runId, at: new Date().toISOString(),
    device: persona.device.playwright, viewport: device.viewport,
    url_path: path, fragment: 'fictional token, never sent to the server',
    http_status: status, load_ms: loadMs, error: resp.error || null,
    ...m, pen_click: pen, pen_click_error: penError,
    console_errors: consoleErrors, failed_local_requests: failed,
    blocked_external_requests: blocked,
  };
  await writeFile(join(out, 'observations.json'), JSON.stringify(record, null, 1) + '\n');
  await context.close();
  return record;
}

const personas = JSON.parse(await readFile(join(here, 'personas.json'), 'utf8')).personas;
const chosen = args.persona === 'all' || !args.persona ? personas : personas.filter(p => p.id === args.persona);
if (!chosen.length) { console.error(`no persona ${args.persona}`); process.exit(2); }
const runId = args.run || new Date().toISOString().replace(/[-:]/g, '').slice(0, 13) + 'Z';

const server = await serve();
const base = `http://127.0.0.1:${server.address().port}`;
const browser = await chromium.launch();
try {
  for (const p of chosen) {
    const r = await runOne(browser, base, p, runId);
    console.log(`${p.id}: ${r.http_status} in ${r.load_ms} ms, ${r.paragraphs} paragraphs (${r.paragraphs_with_own_id} with an id), pen: ${r.pen_click}, blocked ${r.blocked_external_requests.length}, console errors ${r.console_errors.length}`);
  }
} finally { await browser.close(); server.close(); }
