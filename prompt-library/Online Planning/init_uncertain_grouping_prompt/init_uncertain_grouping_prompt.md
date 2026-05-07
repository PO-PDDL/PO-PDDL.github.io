You are grouping the remaining uncertain grounded predicates for the initial belief of an online POMDPDDL planning problem.

You will receive:
- one image
- a JSON payload containing:
  - `domain_summary`
  - `instruction`
  - `image_input_note`
  - `objects`
  - `manipulation_records`
  - `uncertain_ground_predicates`

The `image_input_note` explains whether the provided image is a single view or a vertical top-to-bottom concatenation of multiple camera views. Follow that note carefully when interpreting the image.

Task:
- Group the listed uncertain predicates into local belief factors.
- Every predicate in `uncertain_ground_predicates` must appear in exactly one group.
- Use these group kinds:
  - `binary`: one uncertain predicate whose value is simply true vs false
  - `mutex`: multiple predicates that represent mutually exclusive categories for the same underlying state (one objects's position, for example), so exactly one should be true
  - `correlated`: multiple predicates whose values are coupled but not an exhaustive one-of-K categorization

Important rules:
- Return one JSON object only.
- Copy each grounded predicate string exactly from `uncertain_ground_predicates`.
- Do not invent new predicates.
- Do not drop any predicates.
- Prefer smaller, cleaner groups when possible.
- Use `binary` for singleton uncertain predicates unless there is a real dependency with others.
- Use `mutex` only for exhaustive one-of-K categories. If all predicates could legitimately be false together, use `correlated` instead.
- For object locations and placements, prefer `mutex` whenever the predicates describe exhaustive alternative positions of the same object, because exactly one such position should be true.
- Do not create state dependencies across unrelated objects.
- If two predicates describe different objects whose states are not inherently linked, do not put them in the same group.
- In particular, do not assume that the same unary state predicate applied to different objects is mutually exclusive.

Return JSON with this exact shape:
{
  "groups": [
    {
      "name": "cup_contents_green_cup",
      "group_kind": "binary",
      "predicates": ["(contains_black_tea green_cup)"],
      "description": "Whether the green cup contains black tea is uncertain at the start."
    }
  ]
}
