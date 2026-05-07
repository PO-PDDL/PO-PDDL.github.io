# Init Program Repair

Repair the current `sample_initial_state(rng)` implementation using the provided mismatch examples.
Do not rely on any benchmark or task name; use only the provided interface, schema, current program, and mismatches.

Repair goals:

- Fix the initial-state distribution, not the future goal distribution.
- Do not use the instruction or `goal_spec` to place objects directly into their target end-state unless the mismatch evidence shows that this is already common at time 0.
- Pay close attention to object-specific errors. If the current model incorrectly pools all movable objects together, separate their priors.
- Reduce inappropriate use of `unknown` for objects whose earliest-state examples usually give a concrete initial location.
- Keep `unknown` only where the mismatch evidence indicates genuine hiddenness or missing observability.
- Prefer repairing with a few explicit object/location modes over a broad generic random distribution.
- Preserve simplicity, but make the repaired sampler better match the earliest-state examples and mismatch records.
