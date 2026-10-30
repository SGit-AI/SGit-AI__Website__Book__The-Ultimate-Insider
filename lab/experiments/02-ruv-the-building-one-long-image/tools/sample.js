// Sample every figure in the talk's M01 on its own clock: seek, wait a frame, read each figure's place and colour.
// Writes paths.json: { plan (the drawn building, as SVG), step, end, people: [[{t,x,y,red}]], agents: [...] }. Figures 1 to 22 are the people, 23 on the agents (M01's own order).
const { chromium } = require('playwright')
const fs = require('fs')
const [src, out] = process.argv.slice(2), STEP = 0.1, END = 43
;(async () => {
  const b = await chromium.launch(), p = await b.newPage({ viewport: { width: 1280, height: 720 } })
  await p.goto('file://' + src + '?ruvpaused&theme=light'); await p.waitForTimeout(500)
  const plan = await p.evaluate(async () => {                         // the plan, its labels and the split, as the animation draws them at 3 s
    window.RuvClock.seek(3); await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))
    return [...document.querySelectorAll('#g > g:not([transform])')].slice(0, 3).map(g => g.outerHTML).join('\n')
  })
  const figs = []
  for (let t = 0; t <= END + 1e-9; t += STEP) {
    const row = await p.evaluate(async (t) => {
      window.RuvClock.seek(t); await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))
      return [...document.querySelectorAll('#g > g[transform]')].map(g => {
        const m = /translate\(([-\d.]+) ([-\d.]+)\)/.exec(g.getAttribute('transform'))
        return { on: g.getAttribute('opacity') === '1', x: +m[1], y: +m[2], red: g.firstChild.getAttribute('fill') === 'var(--agent)' }
      })
    }, +t.toFixed(2))
    row.forEach((f, i) => { (figs[i] = figs[i] || []); if (f.on) figs[i].push({ t: +t.toFixed(2), x: f.x, y: f.y, red: f.red }) })
  }
  await b.close()
  fs.writeFileSync(out, JSON.stringify({ plan, source: src.split('/src/')[1] ? 'src/' + src.split('/src/')[1] : src, step: STEP, end: END, people: figs.slice(0, 22), agents: figs.slice(22) }))
  console.log('figures', figs.length, 'samples', figs.reduce((a, f) => a + f.length, 0))
})()
