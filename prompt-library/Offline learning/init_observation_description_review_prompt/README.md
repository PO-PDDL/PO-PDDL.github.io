# `init_observation_description_review_prompt`

- Stage: `init_observation_learning`
- Agent or module: `LLMInitDescriptionContradictionReviewModule`
- Role: performs a text-only screening pass for contradictions between the initial scene description and candidate initial true facts.
- Main inputs: `record`, `filtered_init_facts`, `candidate_ground_truth_facts`, `predicate_comments`, and `feature_predicate_names`.
- Main outputs: `should_review_with_vlm`, `suspect_contradictions`, and `summary`.
- Related artifacts: contributes to `init_observation_evidence.jsonl` and `init_observation_rule_statistics.json`.
- Note: structurally similar to the passive-observation version, but specifically targets the initial observation at step 0.
