# Annotation files for the RC1 companion

One file per role: `team/conductor/rc1/annotations/<role>.json`. Every file is drafted by a conductor sub-agent reading as that role, never in the member's own voice; the member may adopt, change or withdraw any item at its next wake.

```json
{
  "schema": "the-ultimate-insider/rc1-annotations/v1",
  "role": "historian",
  "drafted_by": "a conductor sub-agent reading as the historian (not the member's own words)",
  "summary": "two or three sentences: what this role thinks of RC1 overall",
  "items": [
    {
      "id": "historian-01",
      "chapter": "03-a-mandate-you-can-read.md",
      "anchor": "one exact sentence copied verbatim from that chapter (used to find its page)",
      "kind": "question | comment | decision | rationale",
      "title": "at most 10 words",
      "body": "at most 120 words: the point, plainly",
      "options": ["A: ...", "B: ..."],
      "recommendation": "which option and why, or empty",
      "answer_space": "lines | none",
      "claim_ids": []
    }
  ]
}
```

- `kind: decision` needs two to four `options`; the companion prints a checkbox beside each.
- `kind: question` gets answer lines; `comment` and `rationale` usually `"answer_space": "none"`.
- A number in `body` must come from `claims/register.json`, with its id in `claim_ids`.
- No em-dashes, British spelling, no private people named, no keys or contact details, never the model's name.
