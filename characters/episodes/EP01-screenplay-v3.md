# EP01 v3: "Filming Shorts with a 6'5" mate" (one-take screenplay)

**Format:** vertical 9:16 YouTube Short, about 31 s, loops.
**Rule:** one locked-off camera (Cam A, the vlog tripod) and one continuous
afternoon. Every cut in the finished Short is a **jump cut inside one master
take**, the way a vlogger trims their own footage. There are no cutaways, close-ups or second cameras.

## Why this structure

- **Static wide frame (Keaton, Tati).** The camera never moves, so the
  audience finds the joke in the frame themselves: a head missing off the
  top, then two heads at the same height. Close-ups gave the joke away and
  broke the "same day" feeling.
- **The comic triple.** Mo tries his intro three times and each attempt is
  cut off harder than the last:
  1. Lanky walks in.
  2. Lanky's knees crack.
  3. Mo says it face down into the carpet.

  The third attempt sets up the reveal. v2 lost the middle attempt, so v3
  restores it.
- **Hidden joins (Hitchcock's *Rope*, *Birdman*).** Joins between
  generations go where something fills the frame: Mo's body walking into the
  lens, or a jump cut on a pause. A join in the middle of a gesture is what
  gives AI away.
- **Push-in reveal.** The ending is the same camera, with Mo walking up to
  it. His face filling the frame is the close-up, earned by the action rather
  than by cutting.
- **Button and loop.** Lanky's line is the button. Mo's dead stare cuts
  straight back to frame 1, "Welcome back to the chan—", so the Short loops.
- **Hook in the first second.** Title text is on screen from frame 1, so the
  headless friend reads as a premise, not a mistake.

## The master take

One continuous Cam A take. Anything marked "have" already exists; only
three new 8 s generations are needed.

| Part | What happens | Source | Status |
|---|---|---|---|
| M1 | Mo's intro; Lanky walks in, head off the top | `SH01_v1_raw` (desk composited) | have |
| M2 | "Is it recording?", look-up, "Where's your head?", "Lower." | `SH02b_v1_raw` → `SH03b_v2_raw` | have |
| M3 | Crouch, "Better?", kneel | `SH03b_v2_raw` → `SH03c_v1_raw` → `SH04a_v1_raw` | have |
| **M4** | **Mo, satisfied, turns to the lens: "Perfect. Welcome back to—" and the knees crack** | **new: clip A** (first = last = `shots/EP01_SH04c_first_frame.png`) | generate |
| M5 | "Me knees!", topple; "Fine. We'll do it lying down." | `SH04c_v1_raw` | have |
| M6 | Mo lies face down: "Welcome back to the chann—" into the carpet | `CT_B_raw` | have |
| **M7** | **Mo lifts his head, gets up, walks to the lens, leans in: "…It's been on landscape."** | **new: clip C** (first = `shots/EP01_CT_C_first_frame.png`) | generate |
| **M8** | **Lanky's curls rise into the frame beside Mo's face: "So I could've stood up?" Mo stares.** | **new: clip D** (Extend C, or first = C's last frame) | generate |

**Cost:** 3 × Veo 3.1 Fast, all **silent**. Every line is laid in from
takes already approved, so the "audio generation failed" outage doesn't
matter. The director's overhead and camera-screen close-ups are retired: they
come from other cameras, and the overhead makes Lanky look Mo's height.

## Generation prompts (Flow, Veo 3.1 Fast, 9:16, audio off)

The same rules apply to all three:
- Don't crop the start frame.
- Put one person's action in each sentence.
- Say who is where on screen.

### Clip A: the second intro attempt (M4)
Frames to Video. **First frame and last frame: `EP01_SH04c_first_frame.png`,
the same image in both slots** (Lanky kneeling).
```
Vertical 9:16. Static locked-off camera on a tripod; the framing never changes.
ON THE LEFT: the shorter man with a neat black beard in the mustard jacket nods, satisfied, turns to face the camera and speaks brightly to it for two seconds like a presenter starting an intro, then suddenly stops mid-word and flinches, glancing down to his left.
ON THE RIGHT: the very tall, thin man with big ginger curls in the teal jacket stays kneeling upright on the carpet, still, mouth closed, the whole time. He never stands up.
Screens: the laptop shows a video editing timeline with no people on screen.
Keep both men's faces, clothing and props exactly as in the first frame. Realistic live-action footage, natural motion.
```
Keep: from the head turn to the flinch. The flinch is the reaction to the
crack, which goes under it in post.

### Clip C: the reveal (M7)
Frames to Video. **First frame: `EP01_CT_C_first_frame.png`** (Mo face down).
Last frame empty.
```
Vertical 9:16. Static locked-off camera on a tripod; the framing never changes.
The shorter man with a neat black beard in the mustard jacket is lying face down on the carpet. He freezes, slowly lifts his head and looks straight at the camera. He gets up, walks around the desk directly towards the camera and leans in until his face fills the frame, looking just below the lens as if reading a small screen. His face falls and he says a few words flatly, then stares into the lens, completely still.
The other man stays lying on the floor, out of sight behind the desk.
Screens: the laptop shows a video editing timeline with no people on screen.
Keep the room and the man exactly as in the first frame. Realistic live-action footage, natural motion.
```
Keep:
- The head lift (the realisation).
- A jump cut to him arriving at the lens.
- His line, then the stare.

The frame where his body fills the lens is the natural cut and join point.

### Clip D: the button (M8)
In Flow, **Extend** clip C. Or use Frames to Video with **C's last frame** as
the first frame; the director extracts it and sends it with the clip.
```
Vertical 9:16. Static locked-off camera on a tripod; the framing never changes.
The shorter man's face fills the left of the frame, staring flatly into the lens, completely still, mouth closed, for the whole shot.
From the bottom right of the frame, the very tall man's big ginger curls and freckled face slowly rise into view beside him, as if he is sitting up from the floor. He says a few words to the camera, then stops.
Realistic live-action footage, natural motion.
```
Keep: the curls rising, his line, and a 1 s stare. Hard-cut on the stare.

## Edit decision list (about 31 s)

The times are the finished Short's. "Jump" means a jump cut inside the master take.

| In | Out | Picture | Sound and caption |
|---|---|---|---|
| 00.0 | 01.2 | M1: Mo's intro | "Welcome back to the chan—". Title on top: **Filming Shorts with a 6'5" mate** (0–2 s) |
| 01.2 | 03.0 | jump → M1: Lanky already half in frame | [friend enters. mostly.] |
| 03.0 | 07.6 | jump → M2: 2b from the look-up to 3b frame 23 | "Is it recording?" / look-up (1.3 s) / "Where's your head?" / "Lower." |
| 07.6 | 11.0 | M3: crouch, "Better?", kneel (descending held 1.2 s) | "Better?" / [continues descending] |
| 11.0 | 13.2 | **M4 clip A**: head turn, line, flinch | "Perfect. Welcome back to—" / CRACK (hold the caption 0.6 s) |
| 13.2 | 17.5 | M5: 4c from frame 0, the topple | [incomprehensible tall-man noises] |
| 17.5 | 19.8 | M5: 4c tail | "Fine." / "We'll do it lying down." |
| 19.8 | 24.0 | M6 clip B: lies face down | [sighs in content creator] / "Welcome back to the chann—" (muffled) |
| 24.0 | 25.0 | **M7 clip C**: head lifts | silence, the realisation |
| 25.0 | 27.6 | jump → C: arrives at the lens, "…It's been on landscape." | line from `SH07a_v1_raw` |
| 27.6 | 29.8 | **M8 clip D**: curls rise, Lanky's line | "So I could've stood up?" from `SH07b_v1_raw` |
| 29.8 | 30.8 | D: Mo's stare | room tone. **Hard cut to 00.0** (loop) |

## Post (the director does this; no generation)

- **Room tone:** one continuous crossfaded bed under the whole Short, the same
  level from start to finish (fixes the dropouts and the 12 dB jump in v2).
- **Grade:** the reel's tone curve and vignette on everything.
- **Captions:** the reel's style, about 15% bigger, raised about 120 px so
  they sit over the dark jeans instead of the laptop screen.
- **Loudness:** −14 LUFS integrated, true peak −1.5 dB.
- **Derivatives:** the same master gives a 12 s teaser (00.0–11.0 plus the
  CRACK), and a "blooper" of the face-down line uncut.
