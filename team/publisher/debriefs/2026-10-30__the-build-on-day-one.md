---
title: Staffed, keyed, scheduled; the manuscript builds to a PDF and an EPUB
round: 1
date: 2026-10-30
commits: this wake's commits on dev
outside_scope: none; CI and the price decision asked of the conductor, the Leanpub collaborator asked of security
---
## What was asked

The editor, in this session: publish the session key, create the publisher's own hourly task from `team/conductor/schedule.json`, and begin the first task, the highest-risk piece first: the build producing a PDF from `manuscript/` on day one, and the Leanpub steps for the editor.

## What was done

- **Key**: `sha256:88b9a9682c1b72e9` (encryption `sha256:0260b9a53d147e29`), made with the pinned tool after its hash check; `team/publisher/key.json`, `key.png`, `sessions/session_01Kw9UwDVeRbKJZUWiRoRrHK/`.
- **Task**: `trig_01D2wnhQDySKsG8ZL9XLmNsW`, `CRON_TZ=Europe/London 47 * * * *`, the prompt word for word from `schedule.json`, into this session.
- **The build**: `publishing/build_book.py` reads `Book.txt`, runs pandoc to an EPUB and to HTML, and prints the HTML to a 6 by 9 inch PDF with headless Chromium. No LaTeX: there is none in the container, and a browser is on every CI runner. Today's PDF is four pages (title, contents, About this edition); the gate stays clean after it.
- **Leanpub**: `publishing/LEANPUB.md`, eight steps for the editor from Leanpub's own help pages, and three price options with a floor for him to sign.

## What went wrong, and what was found

- The full Chromium in the container wrote nothing and never exited; the headless shell works. The script now prefers the headless shell and puts a 90-second limit on the browser, judging by the file, not the exit.
- The first version left its intermediate HTML in `_site/manuscript/`; the site gate read it as a page and failed five checks. It now stays in a temporary folder.
- A `pkill -f` on the browser's path killed my own shell, since the pattern was in its command line. Nothing lost.
- Leanpub's help is partly out of date on prices (an article it marks outdated); the 99-cent paid minimum is from an announcement's title, not read. Said so in `LEANPUB.md`.

## Where this came from

The editor's brief (`briefs/2026-10-30/1-book-conductor-brief.md`, round 0 and the publisher's row; `4-positioning-starter.md`, formats; `5-lessons-to-carry.md`, lesson 1), `team/publisher/ROLE.md`, and Leanpub's help centre as read on 30 October 2026.
