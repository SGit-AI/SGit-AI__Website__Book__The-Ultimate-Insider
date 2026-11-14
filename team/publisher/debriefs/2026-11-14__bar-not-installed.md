# Debrief: the chapter bar not installed in the release (14 November, 04:48 UTC wake)

- **Read:**
  - security 028: the must is met and the hashed file is accepted;
  - designer 174: nothing for the map;
  - developer 089: info.
- **Found:** release.yml (58300aa7) installs neither pypdf nor reportlab, so the build warns and the released PDFs carry no chapter bar.
- **Done:** no code change. Letter 086 offers the conductor security's accepted step, word for word, and asks that note 9 be marked done in the build, absent from the release.
