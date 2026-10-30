# Review of admin/tools/pki-agent.mjs (started)

By security@book.the-ultimate-insider, first wake, 30 October 2026. **For the editor first**: the tool is the editor's own (pki.sgit.ai); any fix is the editor's to make there, and the pinned copy here is refreshed only as `pki-agent.README.md` says. Read only: the copy was not changed. Its hash matched `pki-agent.mjs.sha256` before reading.

Defensive notes only: what each finding is, why it matters, and a fix. No key material is quoted.

## Coverage so far

| Part | Lines | Read |
|---|---|---|
| header, imports | 1 to 34 | yes |
| vendored QR generator (MIT) | from 35 | no |
| keys module (`assets/people/keys.js`): algorithms, identity, PBES2, signatures, the envelope | 2278 to 2568 | yes (second wake), but not the DER helpers line by line |
| message module (`assets/people/message.js`): the inner message, links, invitations, agent QR codes, vault keys in text | 2927 to 3147 | yes (sixth wake) |
| directory module (`assets/people/directory.js`): records, statements, the graph, trust from a pinned root | 2569 to 2926 | yes (seventh wake) |
| evidence module (`assets/people/evidence.js`): checking a website, gist or DNS record by machine | 3148 to 3214 | yes (eighth wake) |
| QR reader (`assets/people/qrread.js`): PNG decode and encode, the QR reading | 3216 to 3433 | yes (ninth wake): the PNG decoder line by line; the QR sampling and the standard's tables for shape only |
| unzip module (`assets/people/unzip.js`) | 3434 to 3500 | yes (ninth wake) |
| key store, argument parser, register, pinned root | 3505 to 3600 | yes |
| self-spawn, commands `submit` to `trust` | 3660 to 3800 | yes |
| remaining commands: `keygen` to `keyfile` and `sign` | 3704 to the end | yes (tenth wake) |

The file says it is generated from the site's own code by `admin/build/gen_agent_tool.mjs`; that generator is not in this repository, so the review is of the output.

## Findings so far

**Most important first: finding 14** (tenth wake): the one finding above low. The others below are in the order they were found.


1. **`submit` does not check the operator against the pinned root** (lines 3735 to 3750). `send` and `seal` call `vouched()`; `submit` takes the operator's record, and its inbox endpoint, from the register as it stands. What travels is the agent's own signed public submission, so no secret is exposed. **Narrowed in the seventh wake:** the register files each record under the fingerprint of the key inside it and checks every statement against that key (`readRecord`, lines 2693 to 2741), and an inbox endpoint must be a bare https host (`shapeProblems`, inbox). So a changed register can withhold or drop the operator's record, not quietly put another inbox in its place without a key matching the operator's fingerprint (see finding 6). Fix, if wanted: run `vouched()` on the operator, as `send` does. Severity: information (was low).
2. **Private halves are written unencrypted when `SG_SEND_PASSPHRASE` is not set** (`saveKey`, line 3529). They are mode 0600 in a 0700 folder, as the header says. In this team's sessions the passphrase is not set, so anything else running in the session's container can read them; the container is the session's own and is reclaimed after it. Documented behaviour, recorded for the register: the control here is the container boundary, not the tool. Severity: information.
3. **`--name=value` flags lose everything after a second `=`** (argument parser, line 3521). A value containing `=` (base64 padding, for one) arrives cut short; the space form `--name value` is unaffected. Fix: split on the first `=` only. Severity: low, correctness.
4. **The register and the root can be moved by the environment** (`PKI_REGISTER`, `PKI_ROOT`, `PKI_AGENT_HOME`, lines 3510 to 3513 and 3575). This is by design and the pinned root keeps `send` and `seal` safe against a changed register; recorded because whoever sets the session's environment holds that choice. Severity: information.

5. **A sealed envelope's own signature covers the ciphertext only** (`seal`, lines 2528 to 2537). The sender signs `c`; the wrapped key `w` and the recipient are outside that signature. **Corrected in the sixth wake:** for the tool's own messages this is already met one layer in. The inner message is signed too, and that signature covers `to` and `at` (`compose`, lines 2980 to 2991; the module's header says so, lines 2940 to 2941); `problems` then flags a message "addressed to another key" (line 3002). What remains is text sealed with `sgit pki encrypt` directly, which has no inner message: there a valid envelope signature says who wrote it, not whom it was for. Severity: information. My second-wake text overstated it for the tool's own messages.
6. **Fingerprints are the first 16 hex digits of the SHA-256** (`fingerprint`, line 2331; `FP`, line 2335). That is 64 bits: ample for telling keys apart by eye, less than a full hash for a pin that must resist someone making a key on purpose to match. The pin is checked against the register's full record, so this is a margin, not a hole. Severity: information.

7. **An invitation link can carry an access key outside its signature** (`invite`, lines 3055 to 3066; `parseInvite`, lines 3068 to 3074). `k=` is an SG/Send access key in the link's fragment, and `n=` a name; neither is signed, as the header says. A fragment is never sent to a server, but the link itself is then a secret: pasted into a public file or a vault on this team, it publishes the key. For this team: an invitation with `k=` belongs in a sealed message, never in `comms/`. The gate's tripwire has no pattern for an access key. Severity: information, and worth one line in `comms/README.md` if the team ever sends invitations.
8. **The vault key finder knows one shape** (`VAULT_KEY_RE`, line 3133): lower-case letters and digits, `16 to 64:6 to 32`. A vault key in any other shape is sent as text rather than as a file. It is the tool's own convenience, not its protection (the message is sealed either way). Severity: information.

9. **An operator's link can name any end date** (`validUntil`, line 2649; `shapeProblems`, link). An agent is operated for 30 days when the operator's link names no `until` (`AGENT_DAYS`, line 2643); a link that names one is taken as written, a year or ten. The short life of an agent's standing is a default, not a limit. For this team the point is moot (no member is enrolled: every `key.json` says `enrolled: false`); it matters the day the editor confirms the team's keys. Fix, if wanted: cap `until` for `operates` at a few weeks in `shapeProblems`. Severity: information.

10. **A claimed domain is not checked to be a bare host name** (`domainOf`, line 3167; the evidence shape in `shapeProblems` limits only its length). The value is lower-cased and loses a scheme and a path, nothing more, so a value carrying other URL parts can name a different host from the one a person reading the record sees. The machine check then reads the host the URL really names, and says so in its detail; the risk is a person trusting the value as written. Fix: accept only a host name (letters, digits, dots, hyphens) for `website` and `dns` evidence, in `shapeProblems`. Severity: low.
11. **A server error on a website check reads as a failed proof** (line 3205). A network failure gives "could not be checked" (`null`), but any non-200 answer, a passing 503 included, gives `false`. The DNS check treats a bad answer as "try the next resolver" instead. Fix: `false` for 404 only, `null` for the rest, as the gist check already does (line 3195). Severity: information.
12. **The DNS second channel is two public resolvers over HTTPS** (line 3179). The pinned root's DNS check (`fromRoot`) is "a second channel under another control"; in practice it is Cloudflare's or Google's answer, read over HTTPS, with no DNSSEC validation in the tool. That is a reasonable channel; it is worth knowing it is theirs. Severity: information.

13. **The PNG reader decompresses with no size cap** (`decodePng`, line 3268; called with `zlib.inflateSync` and no `maxOutputLength` at lines 3633 and 3651). The image's declared size is bounded (40 million pixels, line 3263), but the decompressed image data is not checked against it until after it has all been inflated in memory. An image file a session is handed can therefore make the tool use far more memory than its size suggests, and stop. It is a fault that ends the command, not a disclosure. The zip reader beside it is bounded exactly this way already (line 3637). Fix: pass `maxOutputLength: (w * channels + 1) * h` to the inflate, as `unzip` does. Severity: low.

14. **`keyfile` prints both private halves to standard output, in the clear when no passphrase is set** (`keyfile`, lines 3852 to 3857). Its purpose is to carry a key between machines (`PKI_AGENT_KEY`, header lines 17 to 19); with `SG_SEND_PASSPHRASE` unset, as in every session on this team, it warns on standard error and prints the keys unencrypted anyway. In an agent session, standard output is the session's transcript: one run puts the member's private key there, and from there into anything that quotes the transcript. If the output were committed, the gate's tripwire would catch the PEM header (C6), but the transcript is already outside the repository. No member has a reason to run it (session keys never travel: `pki-agent.README.md`), and none has, as far as the record shows. Fix, for the editor: refuse to run without a passphrase, or write only to a file given with `--out` at mode 0600, never to standard output; and one line in `pki-agent.README.md`: never run `keyfile` in a session. Severity: **medium**. Credit: the Cold-Read team's security member found it first (its `team/security/controls-and-threats.md`, finding K2, rated "high if ever run"); this review had not yet reached the command and confirms it.
15. **Sealing here always skips the trust chain** (`admin/tools/vault_handover.py` lines 20 and 127; `vouched`, line 3598). This team pins no root, so the tool's own protection for `seal` and `send` (finding 4, What held) is bypassed by design with `--unverified`: a vault key is sealed to whatever key a `team/<id>/key.json` names. The check that stands in its place is the conductor reading the member's session folder before sealing (C4). No vault exists now (decision of 30 October: no vaults), so nothing is sealed today. Fix, if vaults return: pin the editor's root and drop `--unverified`. Severity: information. Also from the Cold-Read team's register (K3), confirmed here.

## What held

- The algorithms are standard and in the platform's own WebCrypto, with no hand-made primitives: RSA-OAEP 4096 with SHA-256 for sealing, ECDSA P-256 for signing, AES-256-GCM with a fresh random 96-bit IV per message, PBKDF2-HMAC-SHA256 at 210,000 iterations for a passphrase (lines 2341 to 2343, 2428, 2530). Randomness comes only from `crypto.getRandomValues` (line 2305).
- `checkBundle` refuses a bundle whose fingerprints are not its keys' own, and flags an encryption key under 3072 bits (lines 2373 to 2384).
- `unseal` reports "not checked" rather than "forged" when it has no signer bundle to check against (line 2546).
- The inner message signs `to`, `at` and `expires`, so a shown-again QR code reads as expired and a re-sealed message reads as addressed to someone else (lines 2980 to 3005).
- A record is one key's own: every statement must be signed by the key in the record's first, identity, statement, and written for that record (rule 1, line 2711); a revocation can withdraw only the owner's own statements, and a revoked identity loses its links and inbox (line 2739).
- A link counts only when both records hold one, each pointing at the other (`graph`, line 2787): one side alone is a claim and adds nothing.
- Sealing to an agent is refused when the operator's authorised policy and the agent's claimed policy disagree (`vouched`, line 3603), and when the chain does not end at the pinned root or a person it verified (`trustFrom`, line 2889).
- An evidence check that cannot run says so (`null`, "could not be checked from here"), never "false" (the module's own rule, line 3161); a gist proves nothing unless its owner is the account named (line 3197).
- The zip reader is built for someone else's file: at most 200 entries, 10 MB an entry and 60 MB in all, an entry that inflates past its declared size refused, and names kept as labels, never used as paths (lines 3434 to 3483). One bad entry is that entry's error, not the whole archive's.
- The QR reader corrects no errors, and says why that is safe here: a misread gives text that fails to parse or a signature that fails to check, never a wrong secret, because everything it carries is sealed and signed (lines 3225 to 3229).
- `open --save` writes each attached file at mode 0600 with its name stripped of any path part (line 3850), and a vault key found in a message's text is saved as a file, never printed (line 3847).
- `keygen` says where the private halves are and whether they are encrypted, and keeps them there (lines 3704 to 3712).
- `parseQrText` treats a QR code as data carried by hand: exact keys, exact shapes, a length limit, refusal of anything else before a byte is used (lines 3088 to 3129). The rule the team's own CLAUDE.md states for material is written into the parser here.

- `seal --from-vault` reads the vault key from `sgit vault show-key` into memory and never prints it or writes it to a file (line 3768 on); `send` turns a vault key found in `--text` into an attached file rather than message text.
- `pin` says to pin only a fingerprint given out of band; `fromRoot` trusts the pin over the register's own anchors and checks DNS when the pin names a domain.
- `keygen`, `whoami` and `keyqr` write only under `~/.sg-send/` (or `PKI_AGENT_HOME`), as the README says; confirmed for `keygen` and `keyqr` in this session.

## Next

The DER helpers (2394 to 2495) line by line; the vendored QR generator (MIT, 35 to 2277) is third-party code and is checked for network calls and file writes only. Then the review is complete.
