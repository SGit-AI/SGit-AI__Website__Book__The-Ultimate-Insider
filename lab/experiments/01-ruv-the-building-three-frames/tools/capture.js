// Seek the talk's M01 to fixed times on its own clock (?t= freezes there) and save each frame as PNG.
const { chromium } = require('playwright')
const [src, out, theme] = process.argv.slice(2)
const TIMES = (process.argv[5] || '22.5 30 43').split(' ').map(Number)
;(async () => {
  const b = await chromium.launch()
  const p = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 2 })
  for (const t of TIMES) {
    await p.goto('file://' + src + '?t=' + t + '&theme=' + theme)
    await p.waitForTimeout(600)
    await p.screenshot({ path: `${out}/m01-${theme}-t${String(t).replace('.', '_')}.png` })
  }
  await b.close()
})()
