# EP01 production log

Director's approvals, shot by shot. Crops are straight crops of the approved
Gemini master (no retouching); crop box given as x, y, width, height in the
master's pixels.

| Asset | Status | File | Notes |
|---|---|---|---|
| Still A master v1 | ❌ Rejected | `shots/EP01_A_rejected_faces.png` | Geometry good (feet level, crop works) but **both faces off-model**: Mo rounder/chubbier, smaller eyes, lighter skin, no scar, missing-tooth gap; Lanky rounder face, shorter tighter curls. Approved in error without a face check, then revoked. Keeping it as the base for face-replacement edits |
| Still A v2 (Mo face edit) | ❌ Rejected | | Mo still chubby, small eyes, missing-tooth gap, marks on both brows. Root cause: Mo's DNA text ("full cheeks", "slight belly", "tooth gap") contradicted MO_A1; fixed in mo.md v1.3 |
| Still A retake 2 | 🎭 Became casting master | `casting/CAST_v2_master.png` | Faces didn't match v1, but the new pair were more likeable. **Recast** (Mo v2.0, Lanky v2.0). Heights still wrong (Lanky reads ~178 cm) and room isn't the studio, so not usable as Still A |
| MO_A1 | ✅ Approved | `mo/anchors/MO_A1.png` | After 3 fixes (eyebrow piercing → shaved slit; scattered moles → left-cheek cluster; softbox removed). Face unchanged by edits |
| LK_A1 | ✅ Approved | `lanky/anchors/LK_A1.png` | First take. Face, curls, beard all match casting master |
| MO_A4 | ✅ Approved | `mo/anchors/MO_A4.png` | First take. Face matches MO_A1, marks on his left |
| LK_A4 | ✅ Approved | `lanky/anchors/LK_A4.png` | First take |
| CAST_LINEUP | ✅ Built | `CAST_LINEUP.png` | Composited by the director from MO_A4 + LK_A4 at exact scale (170 / 196 cm) with a height chart. Not generated, so heights can't drift. Top of Mo's head = Lanky's chin |
| STU_A2 (Cam A) | ✅ Approved | `locations/anchors/STU_A2.png` | First take. Laptop instead of monitor; set block updated. Camera plan A–D added to studio.md |
| Still A try (both generated together) | ❌ Rejected | | Mo's face drifted (narrow, lighter, no marks); Mo's head at Lanky's nose again |
| Still A try (framed for Mo, Lanky "out of frame") | ❌ Rejected | | Gemini decapitated Lanky inside the frame. Lesson: Gemini always draws whole people; crop afterwards |
| Lanky plate (Cam A) | ✅ Approved | `shots/EP01_plate_LK.png` | Step 1 of the build-up method: Lanky alone, space on the left |
| Still A master v1 | ❌ Withdrawn | `shots/EP01_A_rejected_mo_small.png` | Approved then withdrawn at the user's call: Mo too small (head at Lanky's upper chest, feet ~20 px further back), reads as a miniature man. Lesson: when *adding* a person, Gemini follows the height instruction almost literally, so state the true target (chin), not an overshoot |
| Still A master v2 | ✅ Approved | `shots/EP01_A_master.png` | Mo re-added to the Lanky plate. Mo's head at Lanky's lower lip/chin, height ratio 0.86 (target 0.87). Duplicate clipboard removed with a one-change edit. Lanky unchanged |
| Still A | ✅ Approved | `shots/EP01_A.png` | Crop at x 168, y 346, 513 × 912 (9:16). Top edge just under Lanky's nose |
| Shot 2 video (Flow) | ⏳ Next | | |
| Still A | ⏳ After anchors | | |
| Still A0 | ⏳ Waiting | | After Still A |

**Approval rule:** every still gets a side-by-side face comparison against the
reference images first. No approval without it.

Known drift accepted for this episode (keep consistent across EP01 only):
- Mo's jacket has hip patch pockets instead of chest pockets.
- Lanky's hair is shorter than the bible (ears visible). Hidden in shots 1–2;
  revisit before any shot that shows his head.
