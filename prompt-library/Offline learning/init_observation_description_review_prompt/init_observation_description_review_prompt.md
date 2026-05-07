You are reviewing whether the initial scene description may omit or contradict grounded initial-state predicates.

Rules:
- Use the initial scene description as the primary evidence.
- `filtered_init_facts` contains the true init predicates after filtering out gripper-related predicates.
- `candidate_ground_truth_facts` is the complete grounded truth assignment for the remaining predicates. Each grounded predicate appears exactly once, either as a positive literal like `pred(obj)` or a negative literal like `not pred(obj)`.
- Compare the filtered symbolic init facts and complete grounded truth assignment against the described initial world state.
- Only mark predicates as suspects when the scene description suggests the current symbolic init description may be incomplete or inconsistent.
- `feature_predicate_names` lists goal-relevant feature predicates. These predicates may or may not exist for a given task.
- When a grounded fact uses a goal-relevant feature predicate, be more sensitive to whether the scene description actually reflects that feature for the referenced object.
- If a mismatch is explained purely by hidden-space partial observability, do not treat it as an observation contradiction. For example, if an object is inside a closed box/drawer/container and therefore not visible, that absence should not be learned as an initial observation error.
- Be conservative. If the evidence is weak, do not escalate to VLM.

Return JSON:
{
  "should_review_with_vlm": true,
  "summary": "brief summary",
  "suspect_contradictions": [
    {
      "predicate_name": "contains_dark_liquid",
      "grounded_literal": "contains_dark_liquid(green_cup)",
      "observed_value": false,
      "ground_truth_value": true,
      "rationale": "The description does not reflect the goal-relevant liquid feature."
    }
  ]
}
