# Gemini Playbook

How to get the most out of Gemini for this cast: stills from Gemini's image
model (Nano Banana), animation from Veo. Every prompt in this folder is
already written in the style below.

## 1. Which model to use

| Job | Use | Why |
|---|---|---|
| Anchor images (building a character) | **Nano Banana Pro** (Gemini 3 Pro Image). In the Gemini app, pick the Pro / "Thinking" model before "Create image" | Best facial fidelity, higher resolution, takes more reference images |
| Everyday shot stills | Nano Banana Pro if you have it; Nano Banana (Flash) works for single-character shots | Flash is faster but drifts more with 2+ people |
| Animation | **Veo** via the Gemini app (photo → video) or **Google Flow** | Keeps the still as frame 1 |

Where to run it:
- **Gemini app / gemini.google.com**: easiest. Chat-based editing.
- **Google AI Studio**: same models, plus an **aspect ratio** and
  **resolution** (1K/2K/4K) setting. Use it for anchors and hero shots when you
  need a specific frame size or 2K+.
- **Flow (labs.google/flow)**: best for video: *Frames to Video* and
  *Ingredients to Video*, plus clip extension and scene building.

## 2. How Gemini reads a prompt

1. **Write sentences, not keyword lists.** Gemini is a language model first.
   "A tired 32-year-old man leans on a diner counter at 2am" beats
   "man, diner, night, tired, 8k, cinematic".
2. **Say what you want, not what you don't.** Gemini handles negatives poorly
   ("no beard" can add a beard). Use positive wording:
   - ✗ *no retouching, no beauty filter* → ✓ *unretouched skin with visible
     pores, fine lines and natural unevenness*
   - ✗ *no background* → ✓ *plain mid-grey seamless studio backdrop*
3. **Use photography language.** Shot size, lens (85mm portrait, 35mm
   environment), camera height, light direction and quality, time of day.
4. **When editing, name what stays and what changes.** "Keep his face, hair,
   build and clothing exactly the same. Change only the background to…"
5. **Point at images by number.** "The man in image 1", "the outfit in
   image 2". Gemini numbers attachments in upload order.
6. **One change per turn** for fixes. Gemini is strongest at small,
   targeted edits in a conversation.

## 3. Reference image limits

| Model | Reference images per prompt | Plan |
|---|---|---|
| Nano Banana Pro | Many (up to ~14, strongest for up to ~5 people) | Single shot: A1 + A4. Two-shot: A1 + A4 of each (4 images) + `CAST_LINEUP.png` |
| Nano Banana (Flash) | Best with **3 or fewer** | Single shot: A1 + A4. Two-shot: MO_A1 + LK_A1 + `CAST_LINEUP.png` |

`CAST_LINEUP.png` is one image of the whole cast standing side by side at
true height (prompt in `CAST.md`). It carries height, build and outfits in a
single reference slot.

## 4. Aspect ratio

**Project default: vertical 9:16**, stills and video alike.

| Image | Ratio | How |
|---|---|---|
| Face anchors (A1–A3, A6) | 3:4 portrait | AI Studio setting, or write "vertical 3:4 portrait photograph" |
| Full-body anchors (A4, A5) | 9:16 | as above |
| Shots for video | **9:16** | Start every shot prompt with "A vertical 9:16 photograph" |
| Cast lineup, set wides | 16:9 | Reference only, never animated |

**The still and the video must have the same ratio.** The video tool picks the
output shape, not the still. When a 9:16 still went into a 16:9 Veo clip in
the first test, Veo reframed it and Mo's head was cut off for the whole clip.
Before generating, set the video to 9:16 (Flow lets you choose; if the
Gemini app only gives you landscape, animate in Flow instead).

Watch out: when you edit from an attached image, Gemini often **keeps that
image's aspect ratio**. For a 9:16 shot built from 3:4 anchors, either set the
ratio in AI Studio, or attach a plain blank 9:16 image **last** and say "use
the frame size of the last image".

## 5. Drift control

- **New chat per scene.** Identity slowly softens over many edits in one
  thread. When it starts, open a new chat and re-attach the anchors plus the
  DNA block. Don't keep correcting in the old chat.
- **Always re-paste the DNA block**, even with images attached. Image +
  text together hold identity much better than either alone.
- **Fix faces with a targeted edit**, not a full regenerate:
  "Keep everything in this image exactly the same. Only adjust the face of the
  man on the left so it matches image 1."
- **Watermark:** Gemini images carry an invisible SynthID mark, and on some
  plans a small visible sparkle in the bottom-right corner. **Crop it off every
  still before animating.** If you don't, Veo bakes it into every frame of the
  clip, and it can't be removed afterwards (this happened in the first test).
- **Mirrored marks:** Gemini sometimes flips a mark to the other side (it
  flipped Lanky's neck mole in the first shoot). Check sides on every image
  and fix with a one-change edit.

## 6. Build a Gem (saves you pasting everything)

Create a Gem called **Mo & Lanky Studio**:
1. Gemini → Gems → New Gem.
2. Paste `gem-instructions.md` into **Instructions**.
3. Upload `GEMINI.md`, `mo/mo.md`, `lanky/lanky.md`, `CAST.md` and every file in
   `locations/` as **knowledge files**.
   If your plan allows images as knowledge, also add each character's A1 and
   A4. Otherwise attach them in each chat.
4. In the Gem, you just write a short brief such as *"SC02 SH04: Mo and Lanky
   arguing at a bus stop in the rain, medium two-shot"* and it writes the full
   Gemini prompt, the Veo prompt and the list of images to attach.

When you add a character, upload their bible to the Gem too.

## 7. Animating with Veo

**Best identity: use the approved still as the first frame.**

- **Gemini app:** attach the still, choose video, and use the Veo prompt
  below. You get a short clip (8–10 seconds) with sound. Check the output is
  9:16 before you generate.
- **Flow → Frames to Video:** approved still as start frame. Optionally make a
  second still (same chat, "same shot, 3 seconds later, he has turned to face
  the camera") as the **end frame** for a controlled move.
- **Flow → Ingredients to Video** (A1 anchors as ingredients) is looser. Use it
  only when a shot can't start from an approved still.
- **Extend** a clip from its last frame rather than generating a new one for
  continuous action.

Veo prompt template:
```
Vertical 9:16. Static locked-off camera. [Shot size, e.g. "Medium two-shot"].
Both men's full heads stay in frame for the entire shot.
[Who does what, in order, using the Veo tag from each bible, e.g.
"Mo, the stocky bearded man in the mustard jacket, lowers his clipboard and
stares at Lanky. Lanky, the very tall freckled man with curly ginger hair in
the teal jacket, holds a can against his forehead and doesn't open his eyes."]
Props: [every prop and who holds it, e.g. "Mo holds the same brown clipboard
in both hands throughout. Lanky holds one silver drinks can in his right
hand."]
Screens: [what every screen shows, e.g. "The monitor shows a video editing
timeline with no people on screen."]
Dialogue: Mo says in a low, dry Birmingham voice: "You said five minutes."
Sound: [ambient sound, e.g. "quiet room tone, a distant car outside"].
Keep both men's faces, hair, clothing and heights exactly as in the first
frame. Realistic live-action footage, natural motion.
```

Veo rules (learned from the first test clips):
- **Match the ratio** of the still and the video (see §4).
- **Lock the camera and the framing** unless the shot needs a move. Veo
  otherwise reframes, and a head can leave the frame.
- **Name every prop and say it stays the same.** In the first test Mo's
  clipboard turned into loose paper halfway through.
- **Say what every screen shows.** A monitor with no instruction showed an
  unscripted person.
- **Faces at least a quarter of the frame height for dialogue.** Wide shots
  (face under ~10% of frame height) are fine for silent beats only.
- **One action per character** per clip. Big head turns and fast motion are
  where faces drift.
- **Refer to each person by their Veo tag** (name + visible traits). Veo
  doesn't know the names on their own.
- **Voices:** put dialogue in quotes after the fixed voice description from
  each bible. Veo voices still vary between clips, so for a series plan to
  replace voices in the edit with one consistent voice per character.
