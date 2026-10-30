# SGit-AI__Website__Book__The-Ultimate-Insider

Repo for **the-ultimate-insider.book.sgit.ai**: the book of *The ultimate insider*, a talk by Dinis Cruz at hack::soho, IOActive London, 29 October 2026. How one person and a ten-agent team built the talk in nineteen hours, and the controls that kept the team in check. First edition on Leanpub, Monday 2 November 2026.

- Run locally: `./run-website-locally.sh`, then open http://localhost:8000.
- Release: push to `dev` (or merge to `main`). CI gates, numbers, tags, builds and deploys; see `.github/workflows/release.yml`. The scheme is the talk's site's: CI owns the version.
- The manuscript: `manuscript/`, in the order of `manuscript/Book.txt` (Leanpub's).
- For agents: `CLAUDE.md`, then `briefs/2026-10-30/README.md`, `REALITY.md`, `BRIEF-CORRECTIONS.md`.
