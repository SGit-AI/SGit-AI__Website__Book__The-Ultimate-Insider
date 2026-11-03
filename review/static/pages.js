// The page-by-page view (developer@book.the-ultimate-insider; source review/static/pages.js, placed in src/static/review/ by
// review/tools/make_review.py): one scene of the edition at a time, previous and next by button or arrow key, the place kept in
// the link's fragment (#p-N). It only shows and hides sections already on the page: no network call, no storage.
(function () {
  var pages = Array.prototype.slice.call(document.querySelectorAll('[data-pg]'));
  if (!pages.length) return;
  var at = document.querySelector('[data-pg-at]'), cur = 0;
  function go(i, push) {
    cur = Math.max(0, Math.min(pages.length - 1, i));
    pages.forEach(function (p, k) { p.hidden = k !== cur; });
    if (at) at.textContent = (cur + 1) + ' of ' + pages.length;
    document.querySelectorAll('[data-pg-prev]').forEach(function (b) { b.disabled = cur === 0; });
    document.querySelectorAll('[data-pg-next]').forEach(function (b) { b.disabled = cur === pages.length - 1; });
    if (push) history.replaceState(null, '', '#' + pages[cur].id);
  }
  function fromHash() {
    var k = pages.findIndex(function (p) { return '#' + p.id === location.hash; });
    go(k < 0 ? 0 : k, false);
  }
  document.querySelectorAll('[data-pg-prev]').forEach(function (b) { b.addEventListener('click', function () { go(cur - 1, true); }); });
  document.querySelectorAll('[data-pg-next]').forEach(function (b) { b.addEventListener('click', function () { go(cur + 1, true); }); });
  document.addEventListener('keydown', function (e) {
    if (e.target.closest && e.target.closest('input, textarea')) return;
    if (e.key === 'ArrowRight') { go(cur + 1, true); e.preventDefault(); }
    if (e.key === 'ArrowLeft') { go(cur - 1, true); e.preventDefault(); }
  });
  window.addEventListener('hashchange', fromHash);
  document.documentElement.classList.add('pg-js');
  fromHash();
})();
