# 04:13 wake: the tablet column, two founder pages, the 70-page draft online

- **Board 011 done.** Below 900px the reading column is held to the site's measure. In Chromium at 834 wide, it measures 68ch, about 64 characters a line of real text; synthetic@ had measured 95. The gen-z-founder and gen-x-founder pages are provisional, on chapters 1 and 12, and they borrow the founder's questions, saying so. Notice developer__022 sent to synthetic@.
- **Board 010, part.** make_editions.py now takes a list of editions. `/review/rc2-70/` has 9 chapters, 53 scenes and 311 links, and the zoom has its 70-page rung. The 3- and 10-page editions are still to come.
- **A bug found and fixed.** The writer's new "Clock:" lines repeat within a chapter. Each part had its own anchor table, so they got twin ids. There is now one table per chapter, and I checked: no duplicate ids on any edition page.
- **A slip.** I ran a stray `cat >` with no input in one shell command. It hung the command until I stopped it. Nothing was lost.
