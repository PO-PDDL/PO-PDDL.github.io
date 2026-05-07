# `precondition_selection_prompt`

- Stage: `precondition_learning`
- Agent or module: `LLMPreconditionSelectionModule`
- Role: selects the final action preconditions from the grounded candidate bundle for a specific action.
- Main inputs: `domain_text`, one `action_schema`, and that action's `candidate_bundle`.
- Main outputs: `selected_precondition_literals` and `selection_summary`.
- Related artifacts: `precondition_learning_summary.json`, plus updated `action_schemas.json`, `action_schemas.pddl`, and `domain_with_observation_actions.pddl`.
- Note: the code strictly enforces that selected literals must come from the provided candidate set.
