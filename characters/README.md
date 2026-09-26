# Character Bible

The single source of truth for every recurring character. Built for photoreal,
human-scale characters generated in Gemini (image) and animated in any
image-to-video tool.

**The rule:** the text blocks and the approved anchor images in this folder are
the character. If a shot doesn't match them, the shot is wrong, not the bible.

## Folder layout

```
characters/
├── README.md            ← this workflow
├── _TEMPLATE.md         ← copy this to add a new character
├── CAST.md              ← heights, contrasts, two-shot rules for the whole cast
├── mo/
│   ├── mo.md            ← Mo's bible (DNA block, wardrobe, anchor prompts)
│   └── anchors/         ← approved anchor images: MO_A1.png, MO_A2.png …
├── lanky/
│   ├── lanky.md
│   └── anchors/         ← LK_A1.png, LK_A2.png …
└── shots/               ← finished stills, named SC01_SH03_v2.png
```

## Workflow

### Phase 1: Build each character (once)

1. Open a **new** Gemini chat for the character.
2. Run prompt **A1** (front portrait) from their bible. Regenerate until it's
   right. A1 is the master face, so everything else copies it.
3. In the **same chat**, run A2 → A6 in order. Each one says "same person as the
   previous image."
4. Reject any image where the face drifts from A1. Don't try to fix it by
   editing; just regenerate.
5. Save the approved images into `anchors/` with the exact file names listed.
6. Tick the approval checklist in the bible and set status to `LOCKED`.

After a character is `LOCKED`, the DNA block and anchors never change. Changes
make a new version (`MO v2`). Keep old anchors, rename to `MO_v1_A1.png`.

### Phase 2: Make shots (every time)

1. New Gemini chat per scene (not per project; long chats drift).
2. Attach anchors: **A1 + A4** for a single character. For a two-shot, attach
   **A1 + A4 of each** (4 images) and name them in the prompt.
3. Use the shot prompt template below.
4. Check against the approval checklist. Save to `shots/`.
5. Animate: use the approved still as the **first frame** in image-to-video.
   Never give the video tool a sheet or a raw text description.

### Shot prompt template

```
Image 1 and 2 are [NAME]. Keep his exact face, build, skin, hair and
[WARDROBE CODE] outfit, identical to the reference images.

[DNA BLOCK, pasted exactly]

Scene: [where, time of day]
Action: [what he's doing, expression]
Camera: [shot size, lens, angle], photographed on a full-frame camera,
natural light, real skin texture, no retouching, no beauty filter.
Change only the scene, pose and expression.
```

Two-shot version: see `CAST.md`.

## Realism rules (for all characters)

- Always include: *real skin texture, visible pores, natural asymmetry, no
  retouching, no beauty filter, photographed not rendered*.
- Never use: *beautiful, perfect, flawless, handsome, stunning, 8k,
  hyper-detailed, cinematic masterpiece*. These words push faces towards a
  generic "AI face" and wipe out identity.
- Give lens and shot size (35mm / 50mm / 85mm). Lens changes face shape, so
  use **85mm for close-ups** and **35–50mm for mediums/wides**, and stay
  consistent.
- Every character has **asymmetric anchors** (a scar, a mole on one side, a
  chipped tooth). They're what makes the model see one specific person.
- Faces smaller than ~15% of frame height lose identity. For wide shots, plan a
  face-fix pass or cut to a closer shot.

## Adding a new character

1. Copy `_TEMPLATE.md` into `characters/<name>/<name>.md`.
2. Give them a 2-letter code (MO, LK, …) and check in `CAST.md` that they
   contrast with everyone else: different skin tone or hair or build, and a
   different signature colour.
3. Add them to the height chart in `CAST.md`.
4. Run Phase 1.
