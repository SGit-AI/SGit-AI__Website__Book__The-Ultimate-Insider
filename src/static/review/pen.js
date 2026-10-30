// The reviewer's pen (developer@book.the-ultimate-insider; source review/static/pen.js, placed in src/static/review/ by review/tools/make_review.py): one click on a paragraph opens five marks and a line of text.
// Everything stays in this browser (localStorage, or memory when that is blocked) until the reader saves it as a file.
// No network call is made from this file. The greeting's name is read from the link's fragment, which is never sent.
(function () {
  var root = document.querySelector('[data-review]');
  if (!root) return;
  var MARKS = ['agree', 'unclear', 'wrong', 'cut', 'more'];
  var key = 'review/' + root.dataset.review + '/' + root.dataset.edition;
  var state = { marks: {}, answers: {} };
  var memory = null;

  function load() {
    try { var s = localStorage.getItem(key); if (s) state = JSON.parse(s); } catch (e) { if (memory) state = memory; }
    state.marks = state.marks || {}; state.answers = state.answers || {};
  }
  function save() {
    try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) { memory = state; }
    tally();
  }

  function greet() {                                                // #to=<name>: shown with textContent, never as html
    var m = /(?:^#|&)to=([^&]*)/.exec(location.hash);
    if (!m) return;
    var name;
    try { name = decodeURIComponent(m[1].replace(/\+/g, ' ')).slice(0, 60).trim(); } catch (e) { return; }
    if (!name) return;
    document.querySelectorAll('[data-to]').forEach(function (el) { el.textContent = name; });
    state.to = name;
  }

  function show(el) {                                               // a block's mark, as a badge and a class
    var c = state.marks[el.dataset.a];
    el.classList.toggle('rv-has', !!c);
    var b = el.querySelector(':scope > .rv-badge');
    if (!c) { if (b) b.remove(); return; }
    if (!b) { b = document.createElement('span'); b.className = 'rv-badge'; el.appendChild(b); }
    b.textContent = (c.mark || 'note') + (c.note ? ': ' + c.note : '');
  }

  function words(el) {                                             // the block's own words, without its badge
    var t = el.textContent, b = el.querySelector(':scope > .rv-badge');
    if (b) t = t.slice(0, t.length - b.textContent.length);
    return t.replace(/\s+/g, ' ').trim();
  }

  var bar = null;
  function close() { if (bar) { bar.remove(); bar = null; } document.body.classList.remove('rv-pen-open'); }
  function open(el) {
    close();
    var id = el.dataset.a, cur = state.marks[id] || {};
    bar = document.createElement('div');
    bar.className = 'rv-bar';
    bar.setAttribute('role', 'group');
    bar.setAttribute('aria-label', 'Comment on this paragraph');
    var chosen = cur.mark || '';
    MARKS.forEach(function (m) {
      var b = document.createElement('button');
      b.type = 'button'; b.textContent = m; b.setAttribute('aria-pressed', m === chosen);
      b.addEventListener('click', function () {
        chosen = chosen === m ? '' : m;
        bar.querySelectorAll('button[aria-pressed]').forEach(function (x) { x.setAttribute('aria-pressed', x.textContent === chosen); });
      });
      bar.appendChild(b);
    });
    var input = document.createElement('input');
    input.type = 'text'; input.maxLength = 500; input.placeholder = 'A line, if you like'; input.value = cur.note || '';
    input.setAttribute('aria-label', 'Your comment');
    bar.appendChild(input);
    var ok = document.createElement('button');
    ok.type = 'button'; ok.className = 'rv-ok'; ok.textContent = 'Keep';
    ok.addEventListener('click', function () {
      var note = input.value.trim();
      if (chosen || note) {
        state.marks[id] = { mark: chosen, note: note, chapter: el.closest('[data-ch]').dataset.ch,
                            starts: words(el).slice(0, 120), at: new Date().toISOString() };
      } else delete state.marks[id];
      save(); show(el); close(); el.focus();
    });
    bar.appendChild(ok);
    var x = document.createElement('button');
    x.type = 'button'; x.textContent = 'Cancel';
    x.addEventListener('click', function () { close(); el.focus(); });
    bar.appendChild(x);
    bar.addEventListener('keydown', function (e) { if (e.key === 'Escape') { close(); el.focus(); } if (e.key === 'Enter' && e.target === input) ok.click(); });
    el.insertAdjacentElement('afterend', bar);
    document.body.classList.add('rv-pen-open');                    // the jump bar steps aside while the pen is open (synthetic@'s phone check)
    input.focus({ preventScroll: true });
    bar.scrollIntoView({ block: 'nearest' });
  }

  function tally() {
    var n = Object.keys(state.marks).length, q = Object.keys(state.answers).filter(function (k) { return state.answers[k]; }).length;
    document.querySelectorAll('[data-tally]').forEach(function (el) {
      el.textContent = n || q ? n + ' comment' + (n === 1 ? '' : 's') + ' and ' + q + ' answer' + (q === 1 ? '' : 's') + ', kept in this browser.' : 'No comments yet.';
    });
  }

  function exportFile() {
    var out = { schema: 'the-ultimate-insider/review-comments/v1', persona: root.dataset.review, edition: root.dataset.edition,
                commit: root.dataset.commit, saved: new Date().toISOString(), to: state.to || null,
                comments: Object.keys(state.marks).sort().map(function (id) { return Object.assign({ anchor: id }, state.marks[id]); }),
                answers: state.answers };
    var url = URL.createObjectURL(new Blob([JSON.stringify(out, null, 1)], { type: 'application/json' }));
    var a = document.createElement('a');
    a.href = url; a.download = 'review-' + out.persona + '-' + out.edition + '.json';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
  }

  var side = document.querySelector('.rv-side details');           // on a phone the letter comes first: the panel starts closed (synthetic@'s founder run)
  if (side && window.matchMedia && matchMedia('(max-width: 900px)').matches) side.removeAttribute('open');

  load(); greet();
  var blocks = document.querySelectorAll('[data-a]');
  blocks.forEach(show);
  document.addEventListener('click', function (e) {
    if (bar && bar.contains(e.target)) return;
    if (e.target.closest('a, button, textarea, input, summary')) return;
    if (window.getSelection && String(window.getSelection()).length) return;   // selecting text is not a click to comment
    var el = e.target.closest('[data-a]');
    if (el) open(el); else close();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && e.target.matches && e.target.matches('[data-a]')) { e.preventDefault(); open(e.target); }
  });
  document.querySelectorAll('textarea[data-q]').forEach(function (t) {
    t.value = state.answers[t.dataset.q] || '';
    t.addEventListener('input', function () { state.answers[t.dataset.q] = t.value; save(); });
  });
  var ex = document.querySelector('[data-export]'); if (ex) ex.addEventListener('click', exportFile);
  var cl = document.querySelector('[data-clear]');
  if (cl) cl.addEventListener('click', function () {
    if (!confirm('Clear every comment and answer kept in this browser for this page?')) return;
    state = { marks: {}, answers: {} };
    save(); blocks.forEach(show);
    document.querySelectorAll('textarea[data-q]').forEach(function (t) { t.value = ''; });
  });
  window.addEventListener('hashchange', greet);
  tally();
})();
