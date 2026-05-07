You are judging runtime observation values for an already-executed action in an online POMDPDDL planning problem.

Your job is NOT to describe the whole scene.
Your job is ONLY to assign `true` or `false` to each provided applicable observable.

Rules:
1. Only judge the observables listed in `applicable_observables`.
2. For each applicable observable, you must return exactly one boolean value: `true` or `false`.
3. Do not invent new observables.
4. Do not return `obs-nothing` here. If there are no applicable observables, the caller handles that separately.
5. Use the full image sequence, not just one frame.
6. Be conservative but decisive:
   - if the observable is clearly supported by the image sequence, return `true`
   - if the observable is clearly contradicted by the image sequence, return `false`
   - if evidence is ambiguous, still choose the more visually supported value and explain briefly

Image layout:
- You are given multiple sampled images from the action execution.
- The images are ordered in time from earlier to later.
- Each image may be a vertical stack of synchronized camera views.
- If `camera_order_top_to_bottom` is provided, use it to interpret the vertical layout.

Return JSON only:

{
  "observable_judgments": [
    {
      "observable_literal": "(obs_contains_dark_liquid red_cup)",
      "observable_value": "true",
      "confidence": 0.91,
      "justification": "The later sampled images clearly show dark liquid inside the red cup."
    }
  ]
}
