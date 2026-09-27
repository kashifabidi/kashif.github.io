# Character Bible

The single source of truth for every recurring character. Built for photoreal,
human-scale characters made entirely in Google's tools: **Gemini image
(Nano Banana)** for stills and **Veo** (Gemini app or Flow) for video.

**The rule:** the text blocks and the approved anchor images in this folder are
the character. If a shot doesn't match them, the shot is wrong, not the bible.

Start with **`GEMINI.md`**. It covers which model to use, how Gemini reads
prompts, aspect ratios, reference limits, the Gem setup and Veo.

## Folder layout

```
characters/
├── README.md             ← this workflow
├── GEMINI.md             ← Gemini + Veo playbook
├── gem-instructions.md   ← paste into a Gem so it writes prompts for you
├── _TEMPLATE.md          ← copy this to add a new character
├── CAST.md               ← heights, contrasts, lineup, two-shot template
├── episodes/           ← scripts and shot lists (EP01-tall-mate.md …)
├── locations/
│   ├── studio.md         ← set bible: fixed room description, props, screens
│   └── anchors/          ← STU_A1.png (wide), STU_A2.png (vertical)
├── CAST_LINEUP.png       ← whole cast at true height (made after anchors lock)
├── mo/
│   ├── mo.md             ← Mo's bible (DNA, voice, wardrobe, anchor prompts)
│   └── anchors/          ← MO_A1.png … MO_A6c.png
├── lanky/
│   ├── lanky.md
│   └── anchors/          ← LK_A1.png … LK_A6c.png
└── shots/                ← SC01_SH03_v2.png (stills) and .mp4 (Veo clips)
```

## Workflow

### Phase 1: Build each character (once)

1. Open a **new Gemini chat** with the **Pro image model**
   (Nano Banana Pro) selected. Use AI Studio if you want to set aspect ratio
   and resolution directly.
2. Paste prompt **A1** from the bible. Regenerate until it's right.
   A1 is the master face, and everything else copies it.
3. In the **same chat**, run A2 → A6 in order.
4. Reject any image where the face drifts from A1. Regenerate it rather than
   trying to fix it.
5. Save approved images into `anchors/` with the exact file names listed.
6. Tick the approval checklist and set the status to `LOCKED`.
7. When every character is locked, make `CAST_LINEUP.png` (prompt in
   `CAST.md`).

After a character is `LOCKED`, the DNA block and anchors never change. Changes
make a new version (`MO v2`). Keep the old anchors, renamed `MO_v1_A1.png`.

### Phase 2: Make shots (every time)

1. Open your **Mo & Lanky Studio** Gem (see `GEMINI.md` §6) and give it a
   short brief. It returns the images to attach, the image prompt, the Veo
   prompt and a continuity checklist.
   Without the Gem, fill in the template below yourself.
2. New Gemini chat **per scene**. Attach the anchors it lists (characters +
   location), paste the image prompt.
3. Check the result against the checklist. Fix single problems with a
   one-change edit. Save to `shots/`.
4. Animate in Veo with the approved still as the **first frame**
   (Flow → Frames to Video, or the Gemini app). **Output must be 9:16 to
   match the still.** Use the Veo template and rules in `GEMINI.md` §7.

### Single-character shot template

Attach `XX_A1.png` and `XX_A4.png`.
```
A vertical 9:16 photograph. Images 1 and 2 are [NAME]; keep his face, body,
skin, hair and clothing exactly as in them.

[DNA block, pasted exactly]

He wears [wardrobe wording]. [Set block from locations/, or a scene
description.] [Action and expression.] [Props and who holds them.]

[Shot size], shot on a [85mm for close-ups / 35–50mm for mediums and wides]
lens at [camera height], [lighting]. Unretouched skin with visible pores, fine
lines and natural unevenness. A realistic photograph taken on a full-frame
digital camera.
```

Two-shot template: see `CAST.md`. Veo template: see `GEMINI.md` §7.

## Realism rules (for all characters)

- Always end image prompts with: *Unretouched skin with visible pores, fine
  lines and natural unevenness. A realistic photograph taken on a full-frame
  digital camera.*
- Use positive wording only. Gemini often ignores or inverts "no X".
- Never use: *beautiful, perfect, flawless, handsome, stunning, 8k,
  hyper-detailed, masterpiece*. These words push faces towards a generic
  "AI face" and wipe out identity.
- Always name a lens: **85mm for close-ups**, **35–50mm for mediums and
  wides**. Lens changes face shape, so stay consistent.
- Every character has **asymmetric anchors** with a set side. Gemini
  sometimes mirrors them, so check the side on every image.
- Faces smaller than ~15% of frame height lose identity. For wide shots, cut
  to a closer shot, or do a face edit on the still before animating.

## Adding a new character

1. Copy `_TEMPLATE.md` to `characters/<name>/<name>.md`.
2. Give them a 2-letter code and check in `CAST.md` that they differ from
   everyone else on at least 3 axes, with a new signature colour.
3. Add them to the roster and height chart in `CAST.md`.
4. Run Phase 1, then remake `CAST_LINEUP.png`.
5. Upload their bible to the Gem's knowledge files.

## Adding a new location

Copy `locations/studio.md`, write a new set block, make its two empty-room
anchors, and upload it to the Gem.
