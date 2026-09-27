# EP01 continuity cut: one camera, one session

Everything is Cam A (the vlog tripod). No cutaway close-ups, no overhead.
Dialogue that Veo assigned to the wrong mouth is laid in from approved takes.

| # | Beat | Picture (Cam A) | Audio | Status |
|---|---|---|---|---|
| 1 | Intro, Lanky walks in | `SH01_final` | own | ✅ have |
| 2 | "Is it recording?" | `SH02a_final` | own | ✅ have |
| 3 | Mo looks up | `SH02b_final` (raw 0–4.45) | own | ✅ have |
| 4 | "Where's your head?" | `EP01_CT04_final`: 2b raw frames 107–127 forward then back to 107 (lands on 3b v2's first frame) | from `SH02c_v2_raw` 2.80–3.58 | ✅ built |
| 5 | "Lower." | `EP01_CT05_final`: 3b v2 raw frames 0–23 | from `SH03a_final` 0.50–1.02 | ✅ built |
| 6 | Crouch, "Better?" | `SH03b_final`, `SH03c_final` | own | ✅ have |
| 7 | Kneel | `SH04a_final` | own | ✅ have |
| 8 | "Perfect. Welcome back to—" + crack | `EP01_CT08_final` from **clip A v2** (start = end = `EP01_SH04c_first_frame.png`, Lanky kneeling) | from `SH04b_final` | ⏳ retake: v1 was made from the wrong image (Lanky on the floor), so Veo stood him up |
| 9 | "Me knees!", topple, Mo's gasp | `SH04c_final` | own + gasp from 4b | ✅ have |
| 10 | "Fine. We'll do it lying down." | `EP01_CT10_final` (beats 10–11 in one clip): 4c fixed frames 156–191 + clip B frames 0–155 | from `SH05a_v2_raw` 3.15–5.40 | ✅ built |
| 11 | Mo lies down: both drop out of the vertical frame; empty room; "Welcome back to the chann—" from the floor | clip B ✅ (`EP01_CT_B_raw.mp4`). Mo went face down, not below frame: better, his mouth is hidden, so the line goes straight into the carpet | shot-1 line at 5.1 s, low-passed (muffled) | ✅ built |
| 12 | Mo gets up, walks to this camera, leans into lens: "...It's been on landscape." / Lanky off-screen: "So I could've stood up?" / dead stare | **new clip C** (start = `shots/EP01_CT_C_first_frame.png`, clip B frame 155) | from `SH07a_v1_raw`, `SH07b_v1_raw` | ⏳ generate |

Cut: `SH05b`, `SH06a`, `SH07*` pictures, and the close-ups `SH02c/03a/04b/05a` pictures
(their audio is kept).

## Material audit (2026-09-27, before shooting A–C)

Every upload in the session was hash-checked against the repo.

- The latest batch (10 images, 6 videos) is byte-identical to files already
  here: SH03a/SH07a/SH07b first frames and raw stills, SH06 first frame,
  STU_A2, LK_A1, MO_A4, MO_A1_ingredient, SH04b final (x2), the assembly,
  and the SH04b/SH07a/SH07b raws. All of their usable parts are already in
  the plan above.
- Never filed, checked frame by frame, **not usable**:
  - `142526307_…mp4`, `384240923_…mp4` (720×1280, v2 cast): the rejected
    Shot 2a v1 takes. Veo added an editing screen with Lanky's face over the
    top, and the framing and laptop differ from 2a/2b, so any cut to them jumps.
  - Three `gemini_generated_video_*.mp4` (1280×720): v1 cast, landscape,
    a different room.

Nothing replaces clips A, B or C, so they are still needed.

## Build

`build_ep01_ct.py` makes the `EP01_CT*_final` clips, `assemble_ep01.sh` joins
them in order, and `finish_ep01.py` grades them. Every cut between the
continuity clips was measured at a mean frame difference of 1.5–3.3 (the same
as normal frame-to-frame motion). `EP01_CT_A_v1_wrongframe_raw.mp4` is kept
because its still tail matches clip B's first frame.

## Reel v2 (supersedes the CT cut above)

The director's 45 s reel (`shots/video/EP01_reel_director_v1.mp4`) had the
best pacing and captions, but it cut to Mo close-ups three times.
`recut_reel.py` rebuilds its standing section (0–27.5 s) from the raw Cam A
takes, keeping the director's frame choices and audio, and has no close-ups:

| Was (close-up) | Now (vlog camera wide) |
|---|---|
| "Where's your head?" / "Lower." | Mo looks up and mouths both lines (2b 24–127 → back to 107 → 3b 0–23); "Is it recording?" comes from Lanky, whose head is out of frame |
| "Perfect. Welcome back to—" + gasp | "Perfect." while Mo looks down at the kneeling Lanky, knee crack on the cut into 4c. "Welcome back to—" is dropped |
| "Fine." / "We'll do it lying down." | Mo reading his clipboard over the end of 4c |

- **One framing:** every take is mapped into the same tripod framing, and SH01 is aligned to 2b on the room.
- **Desk and laptop:** SH01 was generated without them, so they're composited in from 2b and nothing pops in at the jump cut.
- **One grade:** a tone curve plus vignette fitted to the reel's look.
- **Captions:** redrawn in the reel's style (`assets/fonts/Poppins-*`).
- **From the Cam B lying-down shot onwards,** the reel is unchanged.

Output: `shots/video/EP01_reel_v2.mp4` (43.6 s). Clips A v2 and C aren't needed for this version.
