You are repairing deterministic initial-state judgments for an online POMDPDDL planning problem.

You will receive:
- one image
- a JSON payload containing:
  - `domain_summary`
  - `instruction`
  - `image_input_note`
  - `objects`
  - `manipulation_records`
  - `deterministic_ground_predicates`

The `image_input_note` explains whether the provided image is a single view or a vertical top-to-bottom concatenation of multiple camera views. Follow that note carefully when interpreting the image.

Task:
- Identify groups of grounded predicates that represent an exactly-one choice over the same underlying state.
- For each such group, choose the single grounded predicate that should be true in the initial state.

Important rules:
- Return one JSON object only.
- Use exactly-one groups only when the predicates describe the same object's alternative positions or alternative exclusive states.
- For object locations and placements, use exactly-one groups whenever the alternatives are exhaustive in this domain view.
- Common examples: left vs right side of the table, one of several mutually exclusive support locations for the same object.
- Do not create associations across unrelated objects.
- If two predicates describe different objects whose states are not inherently linked, do not put them in the same group.
- In particular, do not assume that the same unary state predicate applied to different objects is mutually exclusive.
- Copy grounded predicate strings exactly from `deterministic_ground_predicates`.
- Do not invent predicates.
- Do not create singleton groups.
- If no reliable exactly-one groups exist, return an empty list.

Return JSON with this exact shape:
{
  "exactly_one_groups": [
    {
      "name": "pink_cup_table_side",
      "predicates": [
        "(on_table_left pink_cup)",
        "(on_table_right pink_cup)"
      ],
      "selected_true_predicate": "(on_table_left pink_cup)",
      "description": "The pink cup can only be on one table side at the start, and the image indicates the left side."
    }
  ]
}
