You are identifying what an active perception action observed.

You are given:
- the instruction
- the current active-observation action text
- the previous scene description
- the current scene description
- the filtered current symbolic state
- the candidate grounded truth facts with explicit true/false values
- predicate comments
- the currently available observables as reference

Task:
- Compare the previous and current scene descriptions.
- Infer which predicates this active observation action actually observed.
- Only output predicates that this action appears to have revealed or checked.
- This is an active perception action, so you must choose at least one observed predicate.
- Use `available_observables` as a reference for the observable vocabulary that already exists.
- Use commonsense about the action itself.
- The chosen predicate must be something that the agent could reasonably learn by performing this action.
- Do not choose predicates that are merely true in the world but are not what this action is actually inspecting.
- Prefer predicates that match the semantic target of the action.
- Example: for `look into`, `open and inspect inside`, or `check contents`, prefer predicates about contents, containment, visibility, occupancy, or properties of the inspected target or objects revealed by it.
- Example: for `look into the cup`, do not choose unrelated location predicates such as left/right side of a room marker unless the action is explicitly about checking location.
- Be conservative. Do not invent observations that are not supported by the scene descriptions.
- Feature predicates may exist, but they are optional. Only use them when the descriptions support them.
- Gripper-related predicates are excluded and should not appear in the output.

Return JSON only:
{
  "discovered_observations": [
    {
      "predicate_name": "contains_dark_liquid",
      "grounded_literal": "contains_dark_liquid(green_cup)",
      "observed_value": true,
      "rationale": "The current description says the cup contains dark liquid."
    }
  ],
  "summary": "short summary"
}
