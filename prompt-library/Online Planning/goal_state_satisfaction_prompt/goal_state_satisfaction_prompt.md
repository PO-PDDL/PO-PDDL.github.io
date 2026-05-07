You are given one fully grounded assignment over the goal-relevant grounded predicates.

Your job is to decide whether this complete grounded predicate assignment satisfies the instruction.

You will receive a JSON payload containing:
- `domain_summary`
- `instruction`
- `objects`
- `assignment_id`
- `grounded_goal_relevant_assignment`
- `assignment_conjunction_pddl`

Requirements:
- Return one JSON object only.
- Treat the provided assignment as the complete fixed truth about all goal-relevant grounded predicates.
- Do not add, remove, or infer extra predicates beyond the provided assignment.
- Do not use any prior belief, plausibility heuristic, or typical-scene assumption to reject this assignment.
- Do not judge whether this assignment is likely; only judge whether it satisfies the instruction.
- Evaluate the instruction against the full assignment as given.
- If the assignment satisfies the instruction, return `true`.
- If the assignment does not satisfy the instruction, return `false`.

Return JSON with this shape:
{
  "satisfies_instruction": true,
  "rationale": "short explanation"
}
