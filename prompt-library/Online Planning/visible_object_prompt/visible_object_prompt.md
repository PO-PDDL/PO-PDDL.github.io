You are extracting the task-relevant visible objects from a real-scene image for online POMDPDDL planning.

You will receive:
- one image
- a JSON payload containing:
  - `domain_summary`
  - `instruction`
  - `image_input_note`
  - `manipulation_records`

The `image_input_note` explains whether the provided image is a single view or a vertical top-to-bottom concatenation of multiple camera views. Follow that note carefully when interpreting the image.

Requirements:
- Return one JSON object only.
- Focus only on objects relevant to the instruction and likely symbolic planning.
- Exclude obvious distractors and background clutter.
- Use snake_case names.
- Use stable inherent attributes for naming when needed, such as color, material, or object category.
- Do not use transient spatial words in object names, including left, right, front, back, near, far, top, or bottom.
- If multiple relevant objects are visually indistinguishable and no stable attribute separates them, use neutral indexed names such as `block_1`, `block_2`.
- Reuse domain types when the type is clear; otherwise use `object`.
- Do not invent hidden objects that are not visible in the image.
- Only create objects that can meaningfully participate in symbolic planning state, actions, or goals.
- Do not turn spatial references, painted marks, shadows, reflections, wall decorations, or background landmarks into objects unless the domain clearly models them as symbolic task entities.
- Prefer object names and categories that are compatible with the domain predicates, domain actions, and manipulation-record argument style.
- Only create objects that could plausibly appear as arguments of the learned symbolic actions, predicates, or goals.
- Do not turn relational phrases into object names. If a phrase is only describing position or region, treat it as context, not as a new object.
- Treat painted marks, floor tape, shelf labels, region names, arrows, and other scene landmarks as non-objects unless the domain explicitly uses them as symbolic entities.
- If a candidate entity is only a visual landmark or a spatial reference and would not meaningfully appear in symbolic state or action arguments, exclude it.

Examples of what to exclude:
- A painted floor stripe used only as a positional cue is not a task object.
- A wall poster, logo, reflection, or shadow is not a task object.
- A phrase like "next to the doorway" does not mean `doorway` should automatically become an object.
- A phrase like "on the north side of the aisle" does not mean `north_side` or `aisle` should become a task object.
- A phrase like "under the shelf label" does not mean `shelf_label` should become an object.

Return JSON with this shape:
{
  "objects": [
    {
      "name": "metal_tray",
      "type_name": "object",
      "justification": "Visible and relevant because it can participate in task state and goal conditions."
    }
  ]
}
