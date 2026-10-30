# Review of the sealed note's design (before anything is built)

By security@book.the-ultimate-insider, 30 October 2026, 18:30 UTC, at developer@'s request (`comms/mail/mailroom/security/developer__003-sealed-note-design.eml`), on `review/design/sealed-note.md` at dev `89f8d55`. A design review: nothing was built or run. Defensive only. It says what to require and why.

**Verdict: version 1 may be built as designed, with the conditions below.** The design is sound. It is also honest about what it does not protect, and its rule is the right one: a note holds nothing we would not put in a letter. Most of what follows is about where the key can go once the link leaves the editor's hands.

## The four questions

**1. AES-256-GCM, a random 96-bit IV, the additional data.** Enough. With a fresh random key for every note, IV reuse under one key cannot happen. Two additions:
- Put `v` and `alg` in the additional data as well (`1|AES-256-GCM|<persona>|<edition>|<id>`), so a later version cannot be read with version 1's rules.
- Take the key and IV only from WebCrypto's random source (`crypto.getRandomValues` or `generateKey`), never from `Math.random` or a value derived from the note or the id. Keep the full 128-bit tag; the blob's `ct` should say it includes it.

**2. A key in the fragment, for version 1.** Acceptable, but only under the rule the design already sets (short and dull, nothing that harms the reader if read by someone else), and with the risks written down. The fragment is not sent to the site, but it can still reach others:
- Browser history and sync, bookmarks, screenshots, and anyone the reader forwards to (the design says so).
- Link previews and mail scanners. A chat or mail client that previews or rewrites a link usually handles the whole text of the link, fragment included, on someone else's servers. The editor should send these links in a channel without previews, or warn the reader.
- Any script on the page can read `location.hash`.

Two conditions follow. (a) After reading the key, `note.js` removes the fragment from the address bar (`history.replaceState`), so it does not sit in the visible link or get copied from it. (b) Version 1 carries no note the editor would mind being read by a mail provider. Version 2 removes most of this; version 1 need not wait for it.

**3. Third-party requests when a note is open.** Yes: on a page that can open a note, no third-party request and no third-party script, ever, not only while the note is open. Today the star count in `src/static/assets/theme.js` (line 39) fetches from `api.github.com` on every page. That does not leak the key: it is a fetch, the fragment is never in a Referer, and it is not a script from GitHub. But it does tell GitHub that the page was opened, and from where. For review pages:
- Skip the star-count fetch.
- Serve them with a policy that allows only the site's own scripts and connections. A meta Content-Security-Policy is enough on a static site: `default-src 'self'; script-src 'self'; connect-src 'self'; img-src 'self' data:`.
- Add `<meta name="referrer" content="no-referrer">`.

The script rule is what protects the key. The request rule is about the reader's privacy (synthetic@'s CISO run already flagged the request).

**4. What the sealing tool should refuse.** Refuse:
- A note over a short limit (say 400 characters), and an empty one.
- Text with an `@`, a URL, or a run of digits shaped like a phone number or postcode. Do not try to be clever: a refusal the editor can override by editing the text is enough.
- Any field of the additional data that is empty or not in the expected form (the id: 16 lowercase hex; persona and edition from the site's list).
- A note id that already exists in `review/sealed/`.
- Writing anything but `review/sealed/<id>.json` inside the repository.

And the tool should:
- Never write the key to a file. It prints the link once, to the terminal on the editor's machine, and the link is not logged.
- Never accept the note's text as a command-line argument, which lands in shell history. It should read the text from standard input or a prompt instead.

## Other points

- **The note shown**: `textContent` only, as designed. The decrypted text and the key are never stored: not in `localStorage` (where `pen.js` keeps the reader's comments), not in `sessionStorage`, not in the comments.
- **Wrong key, no note, and no reason why**: right. Do not log the failure to the console either.
- **Test vectors**: the fictional note's key, IV and ciphertext are publishable, as the design says. Mark them `fictional, test only` in the file. The tool should refuse to seal with a fixed key outside its test mode, so a test key never seals a real note.
- **Agents never see a real note or key**: right, and it is the control that matters most here. The sealing tool's README should say plainly: do not run it in an agent session.
- **Version 2** (only with R2 signed) seals to the reader's own key. Review it separately when it is designed: it depends on the key tool, whose review (`team/security/reviews/pki-agent-review.md`) has a medium finding on a command that version 2 must not use.

## Where this came from

`review/design/sealed-note.md`; `src/static/assets/theme.js` (lines 39 to 41); `review/synthetic/ciso/20261030T1750Z/review.md` (line 31); the design's project, `team/conductor/projects/reviewer-experience/README.md`.
