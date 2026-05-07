# Online Planning Prompt Index

This directory documents the prompts used by the online-planning path, split across two code-entry routes:

- `scripts/generate_online_problem.py`
- `scripts/run_interactive_executor.py` for runtime observation judgment

Selection rules:

- Follow the current code path from `generate_online_problem.py` into `POMDPDDL.online_planning_agent.cli` and the agents constructed there.
- Include the observation prompt used by `RuntimeObservationJudgmentAgent` in `run_interactive_executor.py`.
- Exclude prompts that exist in `POMDPDDL/online_planning_agent/prompts` but are not used by these requested paths, such as default-policy and runtime-goal prompts.

Prompts included for `generate_online_problem.py`:

- `visible_object_prompt`
- `init_truth_judgment_prompt`
- `init_location_predicates_prompt`
- `init_object_location_judgment_prompt`
- `init_deterministic_grouping_prompt`
- `init_uncertain_grouping_prompt`
- `init_observable_judgment_prompt`
- `goal_relevant_predicates_prompt`
- `goal_relevant_ground_atoms_prompt`
- `goal_mutex_groups_prompt`
- `goal_semantic_prune_prompt`
- `goal_state_satisfaction_prompt`

Prompts included for `run_interactive_executor.py` observation:

- `runtime_observation_judgment_prompt`

Conditional-use notes:

- `visible_object_prompt` is skipped when `--close-domain` is used or when an existing problem file is reused.
- Goal prompts are skipped when `--reuse-problem-file` is used.
- `init_uncertain_grouping_prompt` and `init_observable_judgment_prompt` are used only when the domain has an observation module and `--skip-init-observation` is not set.

Each prompt subdirectory contains:

- A copied `*.md` prompt file.
- A `README.md` note in English describing the corresponding agent, role, inputs, outputs, and trigger conditions.
