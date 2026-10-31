// Prints the personas' debrief (review/synthetic/pdf/debrief.html, made by build_section.py) to
// src/static/personas/personas-rc1-debrief.pdf with Chromium, and a copy beside its source. No network:
// every request leaving the page is blocked.

import { mkdir, copyFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..', '..', '..');
const src  = join(root, 'review', 'synthetic', 'pdf', 'debrief.html');
const out  = join(root, 'src', 'static', 'personas', 'personas-rc1-debrief.pdf');

await mkdir(dirname(out), { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage();
await page.route('**/*', r => r.request().url().startsWith('file:') ? r.continue() : r.abort());
await page.goto(pathToFileURL(src).href, { waitUntil: 'load' });
await page.pdf({ path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
  headerTemplate: '<span></span>',
  footerTemplate: '<div style="font:8px sans-serif;width:100%;text-align:center;color:#555">Synthetic readers: test instruments, never readers · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
  margin: { top: '16mm', bottom: '18mm', left: '16mm', right: '16mm' } });
await browser.close();
await copyFile(out, join(root, 'review', 'synthetic', 'pdf', 'personas-rc1-debrief.pdf'));
console.log(`printed ${out}`);
