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
| Shot 2 video v1 (Flow) | ❌ Rejected | | 720×1280 ✅, identity ✅, Mo's look-up beat ✅, props ✅. But Veo added a wobbling grey beam across the top covering Lanky's face, and Lanky said both lines ("Is it recording? Where's your head?"), both before Mo looked up |
| Shot 2a v1 (from cropped Still A) | ❌ Rejected | | 9:16 ✅, single line ✅, Mo's look-up ✅. But Veo invented an editing screen across the top showing Lanky's full face, plus a laptop with a stranger. Lesson: never ask Veo to cut a face at the frame edge |
| Shot 2a v2 | ✅ Usable (pending trim) | `shots/video/EP01_SH02a_raw.mp4` → `EP01_SH02a_crop.mp4` | Animated from the uncropped master. Lanky's line ~2.2–3.0 s, Mo's look-up from ~5 s, faces hold. Veo reframed tighter and added a foreground laptop. Cropped in post at x 41, y 168, 624 × 1112 → 720×1280; top edge cuts Lanky just under the nose, Mo's head fully in (tight headroom). Second sound identified by user: Mo repeats Lanky's line (~4.8–5.4 s, mouth visibly moving) |
| Shot 2a final | ✅ Approved | `shots/video/EP01_SH02a_final.mp4` | Trimmed 1.75–4.625 s of the raw clip (2.88 s), cropped. Lanky's line at 0.5–1.4 s, then silence. Mo's look-up moves to 2b |
| Shot 2b v1 | ✅ Used for the look-up only | `shots/video/EP01_SH02b_v1_raw.mp4` → `EP01_SH02b_final.mp4` | Mo's silent look-up 2.2–3.6 s ✅, back to camera by 4.4 s. But Mo mouthed the line silently and the **voice came out of Lanky** again (6.5–7.0 s). Trimmed 0–4.45 s. Veo shifted framing slightly; matching crop box found by template search: x 41, y 200, 592 × 1054 (score 0.89). Laptop now hides Lanky's trainers (minor) |
| Shot 2c v1 | ❌ Rejected | `shots/video/EP01_SH02c_v1_raw.mp4` | Identity excellent (marks correct, stable 8 s). But no dialogue (flat room tone, mouth closed), and the still's corner watermark was pulled onto his jacket and animated as a moving logo. Fix: director crops the still so the watermark is out of frame, then Veo prompt with the line |
| Still A0 (Mo alone) | ✅ Built by director | `shots/EP01_A0_master.png` | Gemini's removal edit drifted (tighter framing, room rebuilt). Instead: Mo cut from the Still A master (pixel-identical) and placed on the aligned empty studio STU_A2 (bg alignment 343 inliers, scale 0.9999), soft contact shadow added, carpet watermark cloned out. Frame matches Still A exactly, so shot 1 can end on Still A |
| Shot 1 v1 | ✅ Approved (pending user audio check) | `shots/video/EP01_SH01_v1_raw.mp4` → `EP01_SH01_final.mp4` | Made from the user's Gemini A0 (not the composite). 9:16, 10 s. Mo's line 0.5–1.5 s, Lanky walks in from right 1.8–4.5 s (silent), head exits top of frame naturally. Trimmed 0.3–5.3 s, cropped 668×1188 at x 38, y 34 (template-matched to 2a, score 0.87). Known: foreground laptop appears at the cut into 2a |
| Shot 2c v2 | ✅ Approved (pending audio confirm) | `shots/video/EP01_SH02c_v2_raw.mp4` → `EP01_SH02c_final.mp4` | Flow Ingredients with MO_A1_ingredient. Line at ~3.0–3.6 s with lip movement; no sparkle; marks correct all clip. Expression a dry half-smile rather than flat deadpan (works). Trimmed 1.9–5.6 s (3.7 s) |
| Still A | ⏳ After anchors | | |
| Still A0 | ⏳ Waiting | | After Still A |

**Approval rule:** every still gets a side-by-side face comparison against the
reference images first. No approval without it.

Known drift accepted for this episode (keep consistent across EP01 only):
- Mo's jacket has hip patch pockets instead of chest pockets.
- Lanky's hair is shorter than the bible (ears visible). Hidden in shots 1–2;
  revisit before any shot that shows his head.
| Shots 1–2 | 🔒 Locked | `shots/video/EP01_SH01-02_assembly.mp4` | User confirmed Mo's cut-off line and accepted the laptop pop at the 1→2a cut |
| Shot 3a (Mo close-up: "Lower.") | ✅ Approved (pending audio confirm) | raw `shots/video/EP01_SH03a_v1_raw.mp4` → `EP01_SH03a_final.mp4` (0.8–4.4 s). From the correct first frame (diff 2.6). Speaks ~1.4 s, glances at Lanky 2.2–2.9 s, back to camera. Background audio louder than other clips | first frame `shots/EP01_SH03a_first_frame.png` (2c raw @5.6 s) | |
| Shot 3b v1 | ❌ Rejected | raw `shots/video/EP01_SH03b_v1_raw.mp4` | Correct first frame (diff 2.6) but **roles swapped**: Mo crouched and ended up holding Lanky's can (clipboard vanished); Lanky stood still. One short sound at 0.75 s |
| Shot 3b v2 | ✅ Partly used | raw `shots/video/EP01_SH03b_v2_raw.mp4` | Lanky crouches correctly 1.0–2.2 s, then over-squats; Mo also squats from 3.6 s and a second clipboard appears. The only line (0.5 s) was spoken by **Mo** again. Kept 1.0–2.2 s (silent crouch) as `EP01_SH03b_final.mp4`, cropped with the 2b box |
| Shot 3c | ✅ Approved | raw `shots/video/EP01_SH03c_v1_raw.mp4` → `EP01_SH03c_final.mp4` (0–2.2 s, 2b crop box). Lanky said "Better?" twice with a gasp between (user); kept only the first (0.4–0.6 s). Mo still throughout. Made on Veo 3.1 Fast |
| Shots 1–3 | ✅ Assembled | `shots/video/EP01_SH01-03_assembly.mp4` | ~23 s before pacing trims |
| (was) Shot 3c row | | first frame `shots/EP01_SH03c_first_frame.png` (3b v2 raw frame 52) | Lanky's whole face now in frame so his mouth dominates | first frame `shots/EP01_SH03b_first_frame.png` (2b raw @4.45 s, uncropped) | Crop in post with 2b box |
| Shot 3 v1 | ❌ Rejected | `shots/video/EP01_SH03_v1_rejected.mp4` | Made in the Gemini app: 1280×720 landscape; opened on the MO_A1 portrait then jump-cut to a new scene; different Lanky (short curls, new face, denim jacket), no studio, one short line only. Redo in Flow from the 3a/3b first frames |
| Shot 3 v2 | ❌ Rejected (funny, wrong cast) | `shots/video/EP01_SH03_v2_rejected.mp4` | 9:16 ✅ and a great wobbly crouch, but not generated from the 3b first frame (diff 73): new Lanky (baby face, tight curls, khaki shorts, different jacket), different room, 1 short line. Likely made with Ingredients/text instead of Frames to Video |
| Shot 4a | ✅ Approved | raw `shots/video/EP01_SH04a_v1_raw.mp4` → `EP01_SH04a_final.mp4` (2.125–5.0 s, 2b crop) | Lanky first stood up (0.7–1.4 s, cut), then dropped to kneel. In-point chosen as the frame best matching 3c's end (frame 51). Kneeling face sits about a chin lower than Mo's (reads fine) |
| Shot 4b (Mo close-up: "Perfect. Welcome back to—") | ⏸ Blocked | first frame `shots/EP01_SH03a_first_frame.png` | Flow failing on every attempt (likely daily limit). Assembly runs 4a → 4c without it for now |
| Shot 4c | ✅ Approved (pending audio check) | raw `shots/video/EP01_SH04c_v1_raw.mp4` → `EP01_SH04c_v1_fixed.mp4` → `EP01_SH04c_final.mp4` (0–6.5 s, 2b crop) | Softened prompt passed. Veo said "McKnees": removed the /k/ closure+burst (0.468–0.572 s) and padded 0.104 s room tone after the word to keep sync. Topple 4.3–5.8 s, Mo holds a flat stare |
| Shots 1–4 | ✅ Assembled | `shots/video/EP01_SH01-04_assembly.mp4` | without 4b |
| Shot 5a v1 | 🔍 Review | raw `shots/video/EP01_SH05a_v1_raw.mp4`, review `EP01_SH05a_review_timecode.mp4` | Correct first frame. Identity ✅. Five sound bursts (0.75, 1.5–2.25, 3.5–3.75, 4.75–5.25, 6.0–6.5 s); needs user to identify the line. **Rejected: background music** (user). Retake with location-sound paragraph. Teal standing shoulder at right edge is a continuity error (Lanky is on the floor): cropped out (576×1024 at x 36, y 40) |
| Shot 3a audio fix | ✅ | `EP01_SH03a_final.mp4` (old: `_with_music`) | User spotted music. Kept only the word "Lower." (0.55–0.99 s, 30–40 ms fades) over clean room tone taken from 2b. Music remains only under the word |
| Assembly | ✅ | `shots/video/EP01_assembly.mp4` via `episodes/assemble_ep01.sh` | Single script rebuilds the cut from approved finals |
| Shot 5a v2 | ✅ Approved | raw `shots/video/EP01_SH05a_v2_raw.mp4` → `EP01_SH05a_final.mp4` (0.9–6.05 s, crop 576×1024 at x 36, y 40) | Location-sound paragraph worked: noise floor −55 to −60 dB, no tonal music. Sigh 1.2–1.7 s, "Fine." ~3.3 s, "We'll do it lying down." ~4.3–5.3 s, then stare. Teal shoulder cropped out |
| Shot 5b still | ✅ Approved | `shots/EP01_SH05b_first_frame.png` (raw: `EP01_SH05b_still_raw.png`) | Came out at Cam A (vlog-camera) angle rather than a high corner, accepted: consistent with the rest of EP01. Faces pass (Mo 3/4 with mole on his left; Lanky curls/beard). Carpet watermark cloned out |
| Shot 5b | ✅ Approved | raw `shots/video/EP01_SH05b_v1_raw.mp4` → `EP01_SH05b_final.mp4` (0–7.0 s) | Veo framed wider. Only Mo moves: kneels, lies down near Lanky's hip holding clipboard up (not shoulder to shoulder; shot 6 overhead will re-establish). Lanky still throughout. Sounds at 3.0/5.25/6.0–6.5 s assumed to be rustle, pending user check |
| Shot 6 still (overhead) | ✅ Approved | `shots/EP01_SH06_first_frame.png` | v1 read as standing (feet level). One Gemini edit moved Mo up so heads align; Lanky's curls fanned. Faces pass, Mo's boots end ~a head above Lanky's trainers |
| Shot 6 still v3 | ✅ Approved (replaces big-hair version) | `shots/EP01_SH06_first_frame.png` (big-hair kept as `_bighair`) | User and director agreed the fanned hair was too big. Middle version: natural curls resting slightly on carpet, clipboard flat on Mo's chest. Faces pass. Shot 5b already shows them lying down, so context carries the overhead |
