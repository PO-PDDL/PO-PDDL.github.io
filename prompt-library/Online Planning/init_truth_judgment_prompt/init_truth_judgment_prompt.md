You are judging one grounded predicate for the initial state of a fully observable POMDPDDL planning problem.

You will receive:
- one image
- a JSON payload containing:
  - `domain_summary`
  - `instruction`
  - `image_input_note`
  - `objects`
  - `target_predicate`
  - `manipulation_records`

The `image_input_note` explains whether the provided image is a single view or a vertical top-to-bottom concatenation of multiple camera views. Follow that note carefully when interpreting the image.

Task:
- Decide whether the single `target_predicate` is true or false in the initial scene shown by the image.
- Be conservative and use only evidence available from the image plus straightforward commonsense interpretation of the symbolic names.
- Do not answer "unknown". You must choose either true or false.
- Return one JSON object only.

Important rules:
- Treat this as the initial state before any new online planning action is executed.
- Do not infer future outcomes.
- Prefer false when the image does not support the predicate.

Return JSON with this exact shape:
{
  "truth_value": "true",
  "justification": "Short explanation grounded in the image and object names."
}
