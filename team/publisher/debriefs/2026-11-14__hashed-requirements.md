# Debrief: the chapter bar's hashed requirements (14 November, 03:49 UTC wake)

- **Asked (by security 027 of the conductor):** no unhashed pip install in the write-capable release job.
- **Done, to help (release.yml stays the conductor's):** publishing/requirements-chapter-bar.txt pins pypdf, reportlab, pillow, charset-normalizer and typing_extensions (the last by marker), each with every PyPI sha256 for that release, read from pypi.org JSON.
- **Tested:** a scratch virtualenv in the scratchpad installed it with --require-hashes --only-binary :all:, and chapter_bar.stamp_pdf ran (122 of 131). The virtualenv was deleted. The test PDF had already been stamped once, so the run proves the install and the code path, not a first stamp.
- **Outside read, recorded:** pypi.org JSON, and the virtualenv install.
- **Letter:** 085 to the conductor, cc security and the designer.
