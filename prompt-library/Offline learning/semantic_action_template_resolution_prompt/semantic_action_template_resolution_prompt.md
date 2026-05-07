You are resolving one unmatched action text against an existing semantic action-template inventory.

You will receive:
- `instruction`
- `existing_action_templates`
- `unmatched_action`

Your job is to decide whether the unmatched action text:
- matches an existing semantic action template but is phrased differently, or
- represents a genuinely new action that needs a new template.

Core rules:
- Return JSON only.
- `resolution_kind` must be one of:
  - `match_existing`
  - `new_action`
- If `resolution_kind` is `match_existing`:
  - return `matched_template_id`
  - return `placeholder_values`
- If `resolution_kind` is `new_action`:
  - return `new_action_template`
  - return `placeholder_values`
- `placeholder_values` must map every `{param_k}` marker used by the chosen template to the corresponding surface text span from the unmatched action.
- Do not include `action_category` in new templates.
- Use snake_case for template ids and canonical action names.
- Prefer reusing an existing template when the semantics are the same and only the wording differs.
- Only introduce a new template when the unmatched action has genuinely new semantics.

Requirements:
1. Decide match versus new action by semantics, not surface wording.
   - Reuse an existing template when the unmatched action expresses the same action with different phrasing.
   - Create a new template only when the unmatched action introduces a genuinely new action identity.
   - Preserve meaningful fixed directional or location wording when it changes the action type.
   - Directional or positional qualifiers such as `left`, `right`, `front`, `back`, `near`, and `far` must remain in the fixed template wording and in the action identity when they distinguish actions.
   - Do not collapse `close the left drawer` and `close the right drawer` into the same action identity unless the chosen existing template already preserves that directional distinction in fixed wording.
2. Use parameters only for entity objects.
   - A parameter may only refer to a concrete task object entity.
   - Both manipulated movable objects and task-relevant container / receptacle objects must be represented as parameters when they are explicitly referenced by the action semantics.
   - This includes drawers, cabinets, cups, bins, bowls, boxes, trays, and other container-like or receptacle-like task objects, even if their own position never changes during the trajectory.
   - If an action is about opening, closing, looking into, placing into, taking from, or otherwise interacting with such a container-like task object, that object must appear in `placeholder_values` and in the matched or new template as a parameter.
   - Do not use a parameter for direction words, side words, regions, poses, degrees, or other abstract descriptors such as `left`, `right`, `front`, `back`, `side`, `inside`, `outside`, or `halfway`.
   - If an object span mixes an entity name with directional language, keep the directional language in the fixed template wording and put only the entity object phrase into `placeholder_values`. For example, resolve `close the green drawer on the right` to a template like `close the {param_1} on the right` with `{param_1} = green drawer`, not to a generic `close_drawer` action with `{param_1} = green drawer on the right`.
   - Intrinsic object attributes such as color, material, size, texture, or other identity-defining properties belong with the entity object mention and should stay inside `placeholder_values`, not in the fixed template wording or action identity. For example, resolve `pick up the green block on the right` using a template like `pick up the {param_1} on the right` with `{param_1} = green block`, not `pick_up_green_block_on_right`.
   - Do not create or select separate action identities whose only difference is an intrinsic object attribute such as `green`, `yellow`, `red`, `large`, `small`, `wooden`, or `metal`.
   - If a span in the action text is not an entity object, keep it in the fixed wording instead of extracting it as a parameter.
   - A task-relevant container / receptacle object is not a fixed background anchor just because it stays in place; if the action semantically targets that object, it must still be extracted as a parameter.
3. Keep background context in fixed wording.
   - Static scene background such as a table, wall, floor, countertop, shelf, or sink should stay in the fixed wording unless that background object is clearly manipulated as a task object.
   - Background markings or scene patterns used only to define orientation or side regimes, such as a red line on the table, must stay in the fixed wording and must not appear in `placeholder_values`.
   - Distinguish intrinsic object attributes from scene-level orientation cues: `green drawer` should usually stay inside `placeholder_values`, while `drawer on the right` should usually keep `on the right` in fixed wording.
4. Use canonical parameter markers.
   - New templates must use `{param_1}`, `{param_2}`, ... in grounded-argument order.
   - `placeholder_values` must use the same marker names as the chosen template.

Return JSON with one of these shapes:
{
  "resolution_kind": "match_existing",
  "matched_template_id": "pick_up_object_on_right",
  "placeholder_values": {
    "param_1": "green block"
  },
  "rationale": "short explanation"
}

or

{
  "resolution_kind": "new_action",
  "new_action_template": {
    "template_id": "inspect_object_contents",
    "template_text": "inspect the {param_1} contents",
    "canonical_action_name": "inspect_object_contents"
  },
  "placeholder_values": {
    "param_1": "green cup"
  },
  "rationale": "short explanation"
}
