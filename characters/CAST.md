# Cast

## Roster

| Code | Name | Status | Signature colour | Height |
|---|---|---|---|---|
| MO | Mo | DRAFT | Mustard / ochre | 170 cm (5'7") |
| LK | Lanky | DRAFT | Teal / petrol blue | 196 cm (6'5") |

## Height chart

Heights are real-world scale. In a shot where both stand side by side on flat
ground:

- Mo's **eyes** are level with Lanky's **collarbone / top of chest**.
- The top of Mo's head reaches about Lanky's **chin**.
- Height difference: 26 cm, so Mo is about **87%** of Lanky's height.

Put this sentence in every two-shot prompt:
> Lanky is 196 cm and Mo is 170 cm; the top of Mo's head reaches Lanky's chin.

## Contrast rules (why they don't blend)

Two-person shots swap features between people unless they're clearly
different. Mo and Lanky are built to be opposites on every axis:

| Axis | Mo | Lanky |
|---|---|---|
| Height | Short | Very tall |
| Build | Stocky, broad | Thin, narrow |
| Face | Round | Long, angular |
| Skin | Warm medium-brown | Very pale, freckled |
| Hair | Black, short fade | Copper-ginger, messy, wavy |
| Facial hair | Full short beard | Patchy stubble |
| Colour | Mustard | Teal |
| Posture | Square, planted | Stooped, one leg |

New characters must differ from **every** existing one on at least 3 of these
axes, and use a new signature colour.

## Two-shot prompt template

Attach 4 images in this order: MO_A1, MO_A4, LK_A1, LK_A4.

```
Images 1 and 2 are Mo. Images 3 and 4 are Lanky. Keep each man's face, build,
skin, hair and outfit exactly as in his own reference images. Do not mix their
features.

[MO DNA block]
[LK DNA block]

Mo wears MO-W1. Lanky wears LK-W1.
Lanky is 196 cm and Mo is 170 cm; the top of Mo's head reaches Lanky's chin.

Scene: [where, time of day]
Positions: Mo on the [left/right], Lanky on the [right/left].
Action: [what each one is doing]
Camera: [shot size], 35mm lens, eye level of a 175 cm person, natural light,
real skin texture, no retouching, no beauty filter. Photographed, not rendered.
```

Tips:
- Keep the same left/right positions across a scene (180° rule). It also helps
  the model keep them apart.
- If one face drifts, don't regenerate the whole shot. Edit with
  *"Keep everything the same. Fix only the man on the left so his face matches
  image 1."*
