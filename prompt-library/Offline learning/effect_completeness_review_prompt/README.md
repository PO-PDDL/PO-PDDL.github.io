# `effect_completeness_review_prompt`

- Stage: `manipulation_domain_learning`
- Agent or module: `VLMEffectCompletenessReviewModule`
- Role: checks whether a grounded effect variant is missing an action-relevant post-action state that is visible in the evidence.
- Main inputs: a review job JSON containing `episode_name`, `step_index`, `canonical_action_name`, `effect_bucket`, `variant_rank`, `predicate_inventory`, `predicate_comments`, `object_types`, grounded results, and the corresponding `frame_paths`.
- Main outputs: `should_apply_repair`, `repair_summary`, and `predicate_additions`.
- Related artifacts: if repair is triggered, proposed predicates flow back into predicate inventory and cause effect re-runs; the review summary is stored in `last_review_summary` and later included in final summaries.
- Note: this is one of the few prompts in the current pipeline that can propose expanding the predicate set.
