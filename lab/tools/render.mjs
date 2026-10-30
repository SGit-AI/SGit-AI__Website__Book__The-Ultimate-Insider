// Render the lab's assembled HTML to PDF with Chromium, and refuse it when a rule in lab/README.md is broken:
// text under 9 pt (12 CSS px, SVG text measured at its placed scale), a page whose content overflows, or a page
// count other than expected. node lab/tools/render.mjs <in.html> <out.pdf> <expected pages>
import { createRequire } from 'node:module'
import { pathToFileURL } from 'node:url'
import fs from 'node:fs'
const require = createRequire(import.meta.url)
const { chromium } = require('playwright')
const [, , input, output, expected] = process.argv

const browser = await chromium.launch()
const page = await browser.newPage()
await page.goto(pathToFileURL(input).href)
await page.evaluate(() => document.fonts.ready)
const problems = await page.evaluate(() => {
  const out = [], MIN = 12 - 0.05
  const pages = [...document.querySelectorAll('.page')]
  pages.forEach((p, i) => {
    const b = p.querySelector('.block')
    if (b.scrollHeight > b.clientHeight + 1) out.push(`page ${i + 1}: content overflows the text block by ${b.scrollHeight - b.clientHeight}px`)
    const walker = document.createTreeWalker(p, NodeFilter.SHOW_TEXT)
    for (let n; (n = walker.nextNode());) {
      if (!n.textContent.trim()) continue
      const el = n.parentElement, cs = getComputedStyle(el)
      let px = parseFloat(cs.fontSize)
      if (el instanceof SVGElement && el.getScreenCTM()) px *= el.getScreenCTM().a
      if (px < MIN) out.push(`page ${i + 1}: "${n.textContent.trim().slice(0, 40)}" is ${(px * 0.75).toFixed(2)} pt`)
    }
  })
  return out
})
await page.pdf({ path: output, format: 'A4', printBackground: true, preferCSSPageSize: true })
await browser.close()
const count = (fs.readFileSync(output, 'latin1').match(/\/Type\s*\/Page[^s]/g) || []).length
if (count !== +expected) problems.push(`the PDF has ${count} pages, expected ${expected}`)
if (problems.length) { console.error(problems.join('\n')); fs.unlinkSync(output); process.exit(1) }
console.log(`rendered ${count} pages, all text at 9 pt or more, no page overflows`)
