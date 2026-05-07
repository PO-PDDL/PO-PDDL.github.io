# `episode_effect_delta_prompt`

- Stage: `manipulation_domain_learning`
- Agent or module: `LLMEpisodeStepEffectModule`
- Role: infers the state-delta effect of one action step inside one episode.
- Main inputs: `instruction`, the current `action_schema`, `taxonomy_record`, the scene-grounded `step`, `problem_spec_without_goal`, `goal_facts`, `filtered_effect_candidates`, and optional `allowed_predicates` and `review_guidance`.
- Main outputs: a `manipulation_record`-style object with fields such as `canonical_action_name`, `action_arguments`, `delta_add`, `delta_del`, `success`, and `effect_bucket`.
- Related artifacts: aggregated outputs are written into `manipulation_records.jsonl` and later used in `episode_grounded_effect_learning_summary.json` and `manipulation_effect_statistics.json`.
- Note: this is the core step-level effect-generation prompt in manipulation learning.
