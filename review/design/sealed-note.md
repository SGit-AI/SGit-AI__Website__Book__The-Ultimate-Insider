# The sealed note: a design, for security's review

developer@book.the-ultimate-insider, 30 October 2026. ROLE.md responsibility 2. **Design only: nothing here is built, nothing is sent, and every name in it is fictional.** Nothing is built until security has reviewed this and the editor has signed R1/R2 or said go on the first version (`team/conductor/projects/reviewer-experience/README.md`).

## What it is for

A review page is the same for every reader of a kind (`/review/ciso.html`). The sealed note is the one personal part: a few lines from the editor ("Sam, you asked about the hold at the meetup; chapter 6 is where it lands"). It must be readable by the person holding the link and by nobody else who reads the repository or the site, both of which are public forever.

## Version 1: a key in the link's fragment

1. **Sealing, on the editor's machine, never in an agent session.** A small tool (to be `review/tools/seal_note.mjs`, Node's WebCrypto, no dependencies) takes the note's text and the page it goes with, makes a fresh random 256-bit key and a random 96-bit IV, and encrypts with AES-256-GCM. The additional data is `<persona>|<edition>|<note id>`, so a sealed blob cannot be moved to another page or edition and still open.
2. **What is committed**: only `review/sealed/<note id>.json`, `{v: 1, alg: "AES-256-GCM", persona, edition, id, iv, ct}`. The note id is random (16 hex), never made from a name. No name, no address, no key.
3. **What is sent** (by the editor, by hand, after he signs): the link `.../review/ciso.html#n=<note id>&k=<key, base64url>`. Browsers never send the fragment to the server, and the `Referer` header leaves it out.
4. **Opening, in the reader's browser**: `pen.js` (or a small `note.js` beside it) reads `n` and `k`, fetches `sealed/<n>.json` from the same site, decrypts with WebCrypto and shows the text with `textContent`, never as HTML. A wrong or missing key shows the page without a note, and says nothing about why.
5. **The agents' part**: the tool, the page code and fictional notes only. Real names and real notes stay with the editor; no agent sees a real note's text or key.

## What it protects, and what it does not

| | Protected | Not protected |
|---|---|---|
| Someone reading the repository or the site | the note's text (only ciphertext is public) | that a note exists, its length, its page and when it was committed |
| The site's host and GitHub | the key (the fragment is never sent) | that the page was opened (the site's star count asks GitHub from every page: synthetic@ has written to the conductor about it) |
| Someone the reader forwards the link to | nothing: the link is the key | |
| Later | | the ciphertext is public forever: if the key leaks later (a mail archive), the note opens forever. So a note holds nothing we would not put in a letter |

Because of the last two rows, the design keeps the note short and dull: no address, no contact detail, nothing that would harm the reader if it were read by someone they forwarded the link to. Whether the reader's name belongs in the note at all is the editor's to decide.

## Version 2 (only with R2 signed): sealed to the reader's own key

The reader makes a PKI key at onboarding (pki.sgit.ai, `admin/tools/pki-agent.mjs`). The note is then sealed to their public key (RSA-OAEP wrapping the AES key), so the link carries no secret, a forwarded link opens nothing, and their comments can be signed. Version 1's blob format keeps a `v` field so both can live side by side.

## A fictional worked example (for the tests, not a real note)

Note id `0f3c9a51d2e84b77`, persona `ciso`, edition `RC1`, text "Sam, thank you for the question about the hold; chapter 6 is where it lands." Recipient: Sam Example, who does not exist. The test vectors (key, IV, ciphertext) will be made by the tool when it is built, and are publishable because the note is fictional.

## Questions for security

1. AES-256-GCM, a random 96-bit IV per note, and the additional data above: enough, or something else?
2. Is a key in the fragment acceptable for version 1, given forwarding and browser history, or should version 1 wait for version 2?
3. Should the page drop the star-count request (or every third-party request) when a note is open?
4. Anything in the sealing step that should be refused by the tool (a note over a length, an `@` or a phone-number shape in the text)?
