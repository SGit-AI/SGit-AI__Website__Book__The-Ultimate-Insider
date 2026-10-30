// node wardley_png.js <svg> <png>: render an SVG to a PNG 1600 px wide
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
  for (let i = 2; i < process.argv.length; i += 2) {
    const svg = fs.readFileSync(process.argv[i], 'utf8');
    const vb = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
    const h = Math.round(1600 * vb[2] / vb[1]);
    await page.setViewportSize({ width: 1600, height: h });
    await page.setContent(`<html><body style="margin:0">${svg.replace('<svg ', '<svg width="1600" height="' + h + '" ')}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: process.argv[i + 1], clip: { x: 0, y: 0, width: 1600, height: h } });
    console.log('wrote', process.argv[i + 1], h);
  }
  await browser.close();
})();
