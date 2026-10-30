# Review of admin/tools/pki-agent.mjs (started)

By security@book.the-ultimate-insider, first wake, 30 October 2026. **For the editor first**: the tool is the editor's own (pki.sgit.ai); any fix is the editor's to make there, and the pinned copy here is refreshed only as `pki-agent.README.md` says. Read only: the copy was not changed. Its hash matched `pki-agent.mjs.sha256` before reading.

Defensive notes only: what each finding is, why it matters, and a fix. No key material is quoted.

## Coverage so far

| Part | Lines | Read |
|---|---|---|
| header, imports | 1 to 34 | yes |
| vendored QR generator (MIT) | from 35 | no |
| keys module (`assets/people/keys.js`): algorithms, identity, PBES2, signatures, the envelope | 2278 to 2568 | yes (second wake), but not the DER helpers line by line |
| message, directory, evidence, QR reader, unzip modules | 2569 to 3504 | no; skimmed for network calls and file writes |
| key store, argument parser, register, pinned root | 3505 to 3600 | yes |
| self-spawn, commands `submit` to `trust` | 3660 to 3800 | yes |
| remaining commands | 3800 to the end | no |

The file says it is generated from the site's own code by `admin/build/gen_agent_tool.mjs`; that generator is not in this repository, so the review is of the output.

## Findings so far

1. **`submit` does not check the operator against the pinned root** (lines 3735 to 3750). `send` and `seal` call `vouched()`; `submit` takes the operator's record, and its inbox endpoint, from the register as it stands. What travels is the agent's own signed public submission, so no secret is exposed; the impact is that a changed register could send the submission somewhere other than the operator's inbox. Fix: run `vouched()` on the operator, as `send` does. Severity: low.
2. **Private halves are written unencrypted when `SG_SEND_PASSPHRASE` is not set** (`saveKey`, line 3529). They are mode 0600 in a 0700 folder, as the header says. In this team's sessions the passphrase is not set, so anything else running in the session's container can read them; the container is the session's own and is reclaimed after it. Documented behaviour, recorded for the register: the control here is the container boundary, not the tool. Severity: information.
3. **`--name=value` flags lose everything after a second `=`** (argument parser, line 3521). A value containing `=` (base64 padding, for one) arrives cut short; the space form `--name value` is unaffected. Fix: split on the first `=` only. Severity: low, correctness.
4. **The register and the root can be moved by the environment** (`PKI_REGISTER`, `PKI_ROOT`, `PKI_AGENT_HOME`, lines 3510 to 3513 and 3575). This is by design and the pinned root keeps `send` and `seal` safe against a changed register; recorded because whoever sets the session's environment holds that choice. Severity: information.

5. **A sealed message's signature covers the ciphertext only** (`seal`, lines 2528 to 2537). The sender signs `c`; the wrapped key `w` and the recipient are outside the signature. So a valid signature shows who wrote the message, not whom it was sealed to: a recipient who opens it could pass it on under the same signature. For this team that matters only if a member treats "signed by the conductor" as "meant for me". Fix, if wanted: sign the wrapped key and the recipient's fingerprint with the ciphertext. Severity: information.
6. **Fingerprints are the first 16 hex digits of the SHA-256** (`fingerprint`, line 2331; `FP`, line 2335). That is 64 bits: ample for telling keys apart by eye, less than a full hash for a pin that must resist someone making a key on purpose to match. The pin is checked against the register's full record, so this is a margin, not a hole. Severity: information.

## What held

- The algorithms are standard and in the platform's own WebCrypto, with no hand-made primitives: RSA-OAEP 4096 with SHA-256 for sealing, ECDSA P-256 for signing, AES-256-GCM with a fresh random 96-bit IV per message, PBKDF2-HMAC-SHA256 at 210,000 iterations for a passphrase (lines 2341 to 2343, 2428, 2530). Randomness comes only from `crypto.getRandomValues` (line 2305).
- `checkBundle` refuses a bundle whose fingerprints are not its keys' own, and flags an encryption key under 3072 bits (lines 2373 to 2384).
- `unseal` reports "not checked" rather than "forged" when it has no signer bundle to check against (line 2546).

- `seal --from-vault` reads the vault key from `sgit vault show-key` into memory and never prints it or writes it to a file (line 3768 on); `send` turns a vault key found in `--text` into an attached file rather than message text.
- `pin` says to pin only a fingerprint given out of band; `fromRoot` trusts the pin over the register's own anchors and checks DNS when the pin names a domain.
- `keygen`, `whoami` and `keyqr` write only under `~/.sg-send/` (or `PKI_AGENT_HOME`), as the README says; confirmed for `keygen` and `keyqr` in this session.

## Next

The message module (`message.js`, from line 2927: the inner message, the link, invitations), then the directory module and the remaining commands; one part per wake.
