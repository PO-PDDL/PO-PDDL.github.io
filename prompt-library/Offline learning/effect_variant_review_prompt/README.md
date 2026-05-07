# `effect_variant_review_prompt`

- Stage: `manipulation_domain_learning`
- Agent or module: `LLMEffectVariantReviewModule`
- Role: decides whether multiple learned effect variants for the same action outcome should be merged into one canonical bucket.
- Main inputs: a single review job containing `canonical_action_name`, `success`, multiple `variants`, and the supporting episode or step evidence for those variants.
- Main outputs: `merge_plans`; the current code expects one valid plan that covers all variant ranks in the group.
- Related artifacts: merged effects update `manipulation_records.jsonl` and `manipulation_effect_statistics.json`; the review decision is stored in module memory and later included in summaries.
- Note: this stage normalizes learned effects after aggregation and does not create new predicates.
