// The time left to each date on the page (an element with data-date and a .cd inside), in the reader's browser. Apache-2.0.
(function () {
  function tick () {
    document.querySelectorAll('[data-date]').forEach(function (el) {
      var cd = el.querySelector('.cd'), left = new Date(el.dataset.date) - Date.now()
      if (!cd) return
      if (left <= 0) { el.classList.add('past'); cd.textContent = 'done or under way'; return }
      var d = Math.floor(left / 864e5), h = Math.floor(left % 864e5 / 36e5), m = Math.floor(left % 36e5 / 6e4)
      cd.textContent = (d ? d + ' d ' : '') + h + ' h ' + (d ? '' : m + ' min ') + 'to go'
    })
  }
  tick()
  setInterval(tick, 30000)
})()
