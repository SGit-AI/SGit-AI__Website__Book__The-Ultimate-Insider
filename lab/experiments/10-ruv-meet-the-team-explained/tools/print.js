// Print an experiment's page.html to PDF (A4, the page's own @page margins).
const { chromium } = require('playwright')
const [src, out] = process.argv.slice(2)
;(async () => {
  const b = await chromium.launch(), p = await b.newPage()
  await p.goto('file://' + src); await p.waitForLoadState('networkidle')
  await p.pdf({ path: out, preferCSSPageSize: true, printBackground: true })
  await b.close()
})()
