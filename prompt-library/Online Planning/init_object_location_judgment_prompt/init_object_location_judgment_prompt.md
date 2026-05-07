You are judging all candidate location predicates for one movable object in the initial scene of a POMDPDDL planning problem.

You will receive:
- one image
- a JSON payload containing:
  - `domain_summary`
  - `instruction`
  - `image_input_note`
  - `objects`
  - `target_object`
  - `fixed_location_predicates`
  - `candidate_location_predicates`
  - `manipulation_records`

The `image_input_note` explains whether the provided image is a single view or a vertical top-to-bottom concatenation of multiple camera views. Follow that note carefully when interpreting the image.

Task:
- Judge each candidate location predicate for the target movable object as true or false in the initial scene.
- Consider all candidate location predicates for this object together, not independently.
- Respect any `fixed_location_predicates` already provided in the payload as fixed prior knowledge and keep the remaining judgments consistent with them.
- Prefer a globally consistent interpretation of the object's initial position.
- Binary predicates should also be considered here when they involve this target movable object and some non-movable reference object.
- Treat the target object as having at most one initial location among the candidate location predicates.
- In normal cases, at most one candidate location predicate should be `true` for this object.
- If several candidate predicates are alternative placements for the same object, choose only the single best-supported one and set the others to `false`.
- Only mark multiple location predicates `true` if they are genuinely simultaneously true and not alternative placements.
- If you believe the target object is not present or not visible in the scene at all, set all of its candidate location predicates to `false`.
- If the image does not support a candidate, prefer false.
- Do not answer "unknown". You must classify every candidate as true or false.

Return one JSON object only with this shape:
{
  "predicate_judgments": [
    {
      "predicate": "(in_front_of green_cup yellow_drawer)",
      "truth_value": "true",
      "justification": "The green cup is visibly in front of the yellow drawer."
    },
    {
      "predicate": "(on_top_of_cup_drawer green_cup yellow_drawer)",
      "truth_value": "false",
      "justification": "The green cup is not resting on top of the yellow drawer."
    }
  ],
  "summary": "short explanation"
}
