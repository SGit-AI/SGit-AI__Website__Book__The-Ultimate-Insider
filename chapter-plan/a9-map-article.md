# A9: the map article, draft 1, for the editor

storyteller@book.the-ultimate-insider, 31 October 2026, the 04:40 UTC wake. **A draft for the editor to read, change or drop. It goes to the newsroom only at his word, through the conductor; nothing has been sent.** Written in his voice (first person), from RC1's map chapter (`team/conductor/rc1/00b-how-to-read-a-map.md`) reshaped by his own words on it (`briefs/2026-10-31__rc1-paper-review/batch-05-pages-10-to-13.md` and `batch-06-pages-14-to-19-wardley-maps.md`; themes T8 and T10 in `team/conductor/rc1/editor-review/notes.json`). Where a sentence is his idea in his words, it is his; the shape and the joins are mine, to be corrected. Figures are the team's existing maps (`team/conductor/rc1/maps/`), named where they would go. One reference is pending: his newsroom article on several kinds of evolution, asked of the researcher.

---

## A graph that learned where things stand

*Draft title. Alternatives: "Every dot is a claim"; "You are already reading Wardley maps" (the punchline, if it may be spent on the title).*

On 29 October I had a talk to give at seven in the evening, and a team of agents building it with me from just after midnight. Let me draw that day the way I first saw it.

At the top, the talk. Under it, what the talk needed: slides, and a player to show them. Under the slides, a site that held them, built and checked every time something changed. Under the site, a pipeline that ran the checks, a host that served the pages, and git, recording every change. A line from one thing to the next means "needs".

*Figure 1: the day as a graph (map 1, then the lower parts of map 5).*

That is a graph. It is useful already: it makes me name what depends on what, instead of assuming it. But move any dot left or right and nothing changes. The slides sit on the left only so their label does not overlap the player's. Position means nothing.

### Now move the dots

Put the things I was inventing that day on the left, and the things I could take for granted on the right. The talk goes far left: it had never been given, and it was being written that morning. The slides sit beside it, made from the talk as data. The site is in the middle: built for this, but in a way the team already knew. The pipeline and the host sit to the right: rented, one choice among many. Git goes far right: standard, free, and so ordinary that nobody thought about it all day.

*Figure 2: the same graph, positioned (map 2).*

Nothing in the picture was added. Only the positions changed, and now every dot says something. "The talk is on the left" says: uncertain, made by hand, mine to get right. "Git is on the right" says: cheap, reliable, someone else's problem. Those two sentences call for opposite kinds of care, and the picture says both at a glance.

That is the whole trick: a map is a top-down tree, or a graph, that becomes a map when position has meaning. A threat model is usually a graph, because where a box sits does not matter. Give left to right a meaning and the same boxes become a map.

### Every dot is a claim, and a claim needs its evidence

When I put a dot somewhere, I am saying something about it, and I should be able to show why. So every dot on my maps links to something: the facts, the evidence, the assumption I am making, or the next map. On the day, the dot for my usage allowance sat low and to the right: a rented resource nobody on the team was watching. The evidence for where it sat was in the record, and at 18:44 that dot is what stopped the team. A map whose dots are not connected to anything is a drawing; a map whose dots are connected is an argument you can check.

### A dot becomes a map

Open any dot and there is a map inside it. The player, one dot on the map of the day, is its own map: the slides it plays, the engine that animates them, the code it was ported from, the browser it runs in. Open the engine and there is another. A dot in one map becomes a map in the next, and so on down, as far as you need to go.

*Figure 3: one dot opening into its own map (to be drawn and animated: this is where visuals do what words cannot).*

This is where maps are most powerful, and where pictures and animation earn their place: you can travel through the system at the level of detail the question needs, and never lose where you are.

### Start from an anchor

Simon Wardley, who created these maps and has published the method openly, recommends starting with a user and their need, because the user is the easiest thing to forget. It is good advice, and the right place to start a first map. But what a map really needs is an anchor: a point of view to read it from. The user is one anchor. A system is another; so is a risk, a team, a vulnerability, a type. Anything you can make a tree of, you can make a map of.

### The axis is not always the same

The four stages a first map usually uses (genesis, custom built, product, commodity) are one evolution axis among several. I have drawn maps whose left-to-right is how well a risk is understood, how settled a timing is, how mature a classification is: different kinds of evolution, each from one to four. *[Reference pending: the newsroom article where I show several kinds of evolution side by side; the researcher is finding it.]* What matters is that position has a meaning you can say out loud.

### Explorers, villagers and town planners

The way I first understood the people who work across a map was as a story.

An explorer sets out alone, or in a small group, into country nobody has crossed. Most attempts fail. Every now and then one gets through, and finds a safe passage to the other side.

Once there is a passage, the villagers can come. They ask different questions: where does everyone sleep, how do we get food, how do we organise ourselves? They make the place liveable, and because it is liveable, more people come.

When enough people arrive, the village needs structure: roads, a hospital, a government. Those are the town planners. They build what lets the place grow without breaking, and once the structure is good, it scales.

One explorer; tens of villagers; then thousands, and then hundreds of thousands, because the structure holds. *(His illustration; the numbers are the story's, not a measurement of anything.)*

*Figure 4: the passage, the village and the town as one map (to be drawn: a diagram, not a list).*

Wardley calls them pioneers, settlers and town planners. On the day, my talk was the explorer's work: a passage found, just. The book that tells it is the villagers' work. Whoever publishes it at scale will be the town planner. That last idea needs the maps above to make sense, which is why it comes last.

### You are already reading Wardley maps

Look back at what you have read. A graph of what needs what. The same graph with its dots moved so that position means something. Dots that link to their evidence. A dot that opens into its own map. An anchor to read it from. An axis that can be about anything that evolves. A story of who works where across it.

That is a Wardley map. You have been reading them since the second figure.

*Further: Simon Wardley's own writing on mapping; my newsroom articles that think with a map, listed under "Thinking with a Wardley map" on newsroom.sgit.ai.*

---

## Notes for the editor (not part of the article)

- **What changed from RC1's chapter, at his word:** the story comes first and the method is named only at the end (T8, "explaining the formula without somebody understanding why they need it"); "a map, not a measurement" is gone and replaced by every dot linking to its evidence (T10); the user and need is Wardley's recommendation, the anchor is the rule (T10); several kinds of evolution (T10); the fractal map (T10); explorers, villagers and town planners told as a story with the numbers he gave (batch 6), the publisher idea last and with a diagram (batch 5, T8).
- **No number in it comes from the register:** the times (19:00, 18:44) are the day's record; 1 to 4 and the story's head counts are his illustration. If the article is used in the book, any count goes through `claims/` first.
- **Figures:** maps 1, 2 and 5 exist (`team/conductor/rc1/maps/`); figure 3 (a dot opening into a map, animated) and figure 4 (the passage, the village, the town) are new, for the designer.
- **Credit:** Wardley is named as the method's creator with his openly published work; the article quotes him nowhere. The pioneers, settlers and town planners are his terms; explorer and villager are the editor's.
- **No claim about others** (T19): the two places that generalised about "people" were rewritten.
- **Length:** about 1,400 words.
