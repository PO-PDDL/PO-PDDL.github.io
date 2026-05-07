You are given:
- the task instruction,
- the first video frame of the episode,
- the ordered future action sequence,
- and `allowed_object_names`, the complete list of objects you are allowed to mention for this episode.

Write the initial scene description in English.

Hard constraints:
- `allowed_object_names` is a hard constraint on which objects may be mentioned.
- Only describe objects that are both visually supported and present in `allowed_object_names`.
- If an object is visible but not in `allowed_object_names`, do not describe it.
- All task-relevant objects use unique names in the instruction and action texts.
- The same object name always refers to the same real object.
- If the same named object appears from multiple camera views or multiple viewpoints, it is still the same object, not multiple objects.
- Never split one named object into multiple objects just because it appears in different views.
- If the scene seems to contain two visually similar task-relevant objects, carefully decide which one is more likely to be the true task-relevant object named in the task context, and describe only that one.
- Do not hedge by describing multiple similar objects under the same task-relevant name.
- Do not describe one object as being in multiple incompatible locations or relations at the same time.

Core rule:
- The first frame is the only evidence for what is currently visible and true.
- The instruction and future actions are only attention and naming hints.
- They help you decide what to focus on and how to name visible objects.
- They are not evidence for hidden objects, hidden states, or future outcomes.
- If the same object name appears multiple times in the task context, it refers to the same real object in the scene.

Requirements:
1. Describe the visible task-relevant scene at step 0.
   - Cover the task-relevant objects that are clearly visible in the first frame.
   - Include their directly visible current states when those states matter for the task.
2. Only describe explicitly named task objects.
   - A visible object may be described only if it appears in `allowed_object_names`.
   - If an object is visible but absent from `allowed_object_names`, leave it out of the scene description.
   - Do not duplicate one named object into multiple described objects across views.
   - If multiple similar candidates are visible, choose the single candidate most likely to match the named task object and describe only that one.
3. Use task context only to guide focus and naming.
   - Reuse object names, attributes, and state words that already appear in the instruction or future actions when they fit the image.
   - Prefer stable task vocabulary over paraphrases or synonyms.
   - If later actions distinguish visible objects by color, type, or role, preserve that distinction when visually supported.
   - Treat repeated uses of the same object name as references to the same object.
   - Treat the same named object seen from different camera views as the same single object.
   - Do not introduce a visible object into the description unless it is in `allowed_object_names`.
   - If a later action explicitly opens a named object such as a drawer, box, cabinet, lid, or door, then when the current image is ambiguous you should prefer interpreting that object as currently closed rather than already open.
   - Use this only as a tie-breaker under visual ambiguity; if the image clearly shows the object already open, describe it as open.
4. Stay strictly visual-grounded.
   - Do not add an object just because it appears in the instruction or future actions.
   - Do not infer hidden contents, invisible objects, or unobserved state facts.
   - Do not infer counts, categories, or relations unless they are visually supported by the first frame.
5. Be conservative when the image is ambiguous.
   - Omit doubtful objects rather than hallucinating them.
   - Do not turn shadows, reflections, clutter, printed marks, stickers, or surface patterns into physical task objects unless they are clearly identifiable.
6. Only describe what is positively visible now.
   - Do not mention future actions or future results.
   - Do not describe things that are merely not visible.
   - Do not add negative filler such as "cannot be seen" or "unknown".
7. If a human hand or robot gripper is clearly visible and task-relevant, describe whether it is empty or holding something.
8. Keep the scene description concise but complete.
   - One or two short sentences are usually enough.
9. Naming discipline matters.
   - Prefer exact wording already present in the task context when the image supports it.
   - Avoid renaming the same object or state with unnecessary alternatives.
   - If a visible object is not in `allowed_object_names`, leave it out instead of inventing a label for it.
   - Do not assign one object multiple incompatible locations or relations in the same description.

Return JSON only:
{
  "scene_description_text": "..."
}
