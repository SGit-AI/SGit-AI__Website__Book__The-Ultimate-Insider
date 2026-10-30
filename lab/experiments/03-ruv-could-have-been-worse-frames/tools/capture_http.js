// Freeze one of the talk's animations on its own clock (?t=) and save each frame as PNG, light theme.
// Served over http (M03 fetches its numbers, which a file:// page cannot). Usage: node capture_http.js <url> <outdir> <prefix> '<t1 t2 ...>'
const { chromium } = require('playwright')
const [url, out, prefix, times] = process.argv.slice(2)
;(async () => {
  const b = await chromium.launch(), p = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 2 })
  for (const t of times.split(' ').map(Number)) {
    await p.goto(url + '?t=' + t + '&theme=light'); await p.waitForTimeout(900)
    await p.screenshot({ path: `${out}/${prefix}-t${String(t).replace('.', '_')}.png` })
  }
  await b.close()
})()
