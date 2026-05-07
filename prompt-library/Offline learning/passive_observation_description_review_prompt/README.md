# `passive_observation_description_review_prompt`

- Stage: `passive_observation_learning`
- Agent or module: `LLMDescriptionContradictionReviewModule`
- Role: performs the first text-only screening pass for possible contradictions between scene descriptions and the grounded state before visual confirmation.
- Main inputs: `record`, `filtered_state_before`, `candidate_ground_truth_facts`, `predicate_comments`, and `feature_predicate_names`.
- Main outputs: `should_review_with_vlm`, `suspect_contradictions`, and `summary`.
- Related artifacts: contributes to passive-observation evidence and downstream `passive_observation_rule_statistics` and `passive_observation_evidence.jsonl`.
- Note: this is the first filtering step before VLM-based confirmation.
