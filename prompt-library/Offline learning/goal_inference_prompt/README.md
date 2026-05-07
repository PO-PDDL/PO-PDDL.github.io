# `goal_inference_prompt`

- Stage: episode problem-context construction inside `manipulation_domain_learning`
- Agent or module: `LLMGoalInferenceModule`
- Role: infers goal facts for a single episode from the task instruction and the already assembled object and initial-fact context.
- Main inputs: `domain_name`, `allowed_predicates`, `instruction`, `objects`, `init_facts`, and optional `review_guidance`.
- Main outputs: `goal_facts`.
- Related artifacts: does not form a standalone stage; the raw output is stored in `goal_inference_raw_output` and later written into episode grounding and effect-learning summaries.
- Note: the code checks that every returned goal fact uses only allowed predicates and known object names.
