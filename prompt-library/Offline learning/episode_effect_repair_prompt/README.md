# `episode_effect_repair_prompt`

- Stage: `manipulation_domain_learning`
- Agent or module: `LLMEpisodeEffectRepairModule`
- Role: jointly repairs init facts, goal facts, and step-level effect records when grounded replay fails or the goal is not satisfied.
- Main inputs: `episode_context`, `problem_spec`, `final_state`, `goal_satisfied`, `action_schemas`, `allowed_predicates`, `manipulation_records`, `grounded_steps`, `validation_steps`, `validation_issues`, and `iteration_history`.
- Main outputs: `should_apply_repair`, `repair_summary`, `init_facts_add/remove`, `goal_facts_add/remove`, `step_effect_repairs`, and `suspected_issue_sources`.
- Related artifacts: successful repairs are reflected in final `manipulation_records.jsonl` and episode-level grounding summaries; the review or repair trace is preserved inside episode result summaries.
- Note: the code validates the response structure and can automatically retry this repair prompt when needed.
