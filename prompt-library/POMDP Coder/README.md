# `POMDP Coder` Prompt Library

This directory mirrors the prompts used by the reproduced `pomdp_coder` pipeline and runtime.

Included scope:

- offline learning prompts for task-interface induction, symbolic grounding, initial proposal, and repair
- online planning/runtime prompts for goal parsing and multimodal observation grounding

Grouping:

- `Offline learning`: prompts used before model assembly
- `Online planning`: prompts used after the learned runtime bundle is executed

Each prompt folder contains:

- the prompt markdown file
- an English `README.md` explaining the role, inputs, outputs, and trigger condition
