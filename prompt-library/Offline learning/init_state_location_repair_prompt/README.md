# `init_state_location_repair_prompt`

- Stage: episode problem-context construction inside `manipulation_domain_learning`
- Agent or module: `LLMInitStateRepairModule`
- Role: repairs the inferred initial true-fact set, especially when location-like facts or the current truth set appear inconsistent.
- Main inputs: `domain_summary`, `episode`, `selected_objects`, `current_true_init_facts`, `grounded_predicates`, and optional `review_guidance`.
- Main outputs: `should_repair`, `init_facts_add`, `init_facts_remove`, and `repair_summary`.
- Related artifacts: not a standalone stage; the raw response is stored in `object_init_raw_llm_outputs["initial_state_location_repair"]`.
- Note: the code filters out invalid additions and removals, so the prompt proposes a repair plan rather than forcing it directly into the state.
