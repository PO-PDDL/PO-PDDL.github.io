# `initial_state_inference_prompt`

- Stage: episode problem-context construction inside `manipulation_domain_learning`
- Agent or module: `LLMInitialStateInferenceModule`, invoked by the default object-init path inside `EpisodeProblemContextModule`
- Role: infers initial true facts for a single episode and provides `problem_spec_without_goal` for later effect grounding.
- Main inputs: `domain_summary`, `episode`, `visible_objects`, `visible_facts`, `latent_objects`, and the default `grounded_predicates` candidate set.
- Main outputs: one of two formats:
  - `predicate_classifications` or the split `location_predicate_classifications` and `other_predicate_classifications`
  - or the legacy `init_facts` format
- Related artifacts: not written as a standalone stage; raw responses are collected into per-episode `object_init_raw_llm_outputs` and later appear in `episode_grounded_effect_learning_summary.json` and related grounding summaries.
- Note: in the current default path, this prompt is mainly used for grounded initial-fact classification over action-argument objects, not for the full visible/latent object inference workflow.
