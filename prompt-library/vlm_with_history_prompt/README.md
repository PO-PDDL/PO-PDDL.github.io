# `vlm_with_history_prompt`

Stage: runtime closed-loop VLM task dispatch

Role:
Asks a multimodal LLM to choose the next executable robot action from a fixed atomic action list, using the current scene images and optional action history.

Trigger condition:
Used by `task_dispatcher.py` when `--vlm_mode` is enabled. The history portion is included when `--vlm_history` is enabled, and reference demonstrations are included when `--vlm_language_history` points to readable episode JSON files.

Major inputs:
- overall instruction
- current scene frames from executor
- task-relevant object list
- available atomic actions
- temporarily forbidden actions
- successful reference scene-description episodes
- history of executed actions and previous VLM reasoning

Major outputs:
- two-line response with `REASONING:` and `ACTION:`
- `ACTION:` is parsed as one exact task from `TASK_LIST`, or `DONE` only after a successful `report-goal`

Runtime assembly note:
The fixed system prompt is stored in `vlm_with_history_prompt.md` and loaded by `task_dispatcher.load_vlm_with_history_system_prompt()`. The user message is assembled dynamically in `task_dispatcher.vlm_select_task(...)` from the latest images, available actions, object list, reference episodes, forbidden actions, and action log.
