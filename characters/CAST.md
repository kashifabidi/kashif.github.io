# Cast

## Roster

| Code | Name | Status | Signature colour | Height |
|---|---|---|---|---|
| MO | Mo | LOCKED (face) | Mustard / ochre | 170 cm (5'7") |
| LK | Lanky | LOCKED (face) | Teal / petrol blue | 196 cm (6'5") |

## Height chart

Heights are real-world scale. When both stand side by side on flat ground:

- Mo's **eyes** are level with Lanky's **collarbone / top of chest**.
- The top of Mo's head reaches about Lanky's **chin**.
- Height difference: 26 cm, so Mo is about **87%** of Lanky's height.

Height sentence (paste into every two-shot prompt):
```
Lanky is 196 cm tall and Mo is 170 cm tall, so when they stand side by side
the top of Mo's head reaches Lanky's chin.
```

## Contrast rules (why they don't blend)

Two-person shots swap features between people unless they're clearly
different. Mo and Lanky are built to be opposites on every axis:

| Axis | Mo | Lanky |
|---|---|---|
| Height | Short | Very tall |
| Build | Solid, broad-shouldered | Thin, narrow |
| Face | Lean, angular, strong jaw | Long, narrow, soft-featured |
| Skin | Warm medium-brown | Very pale, freckled |
| Hair | Black, very short, skin fade | Copper-ginger curls to the collar |
| Facial hair | Full short black beard | Short uneven ginger beard |
| Colour | Mustard | Teal |
| Posture | Square, planted | Stooped or sprawled |

New characters must differ from **every** existing one on at least 3 of these
axes, and use a new signature colour.

## Cast lineup (build once, after all anchors are LOCKED)

One image of the whole cast at true height. In Gemini it carries height,
build and outfits in a single reference slot. Save as
`characters/CAST_LINEUP.png` and remake it whenever a character is added or
changes version.

Attach: MO_A4, LK_A4 (plus A4 of any new character). 16:9.
```
A horizontal 16:9 studio photograph. Image 1 is Mo and image 2 is Lanky. Keep
each man's face, body, skin, hair and clothing exactly as in his own image.
They stand side by side facing the camera in front of a plain mid-grey
seamless backdrop with a subtle white height scale painted on the wall behind
them, marked every 10 cm. Mo stands on the left, Lanky on the right, about
half a metre apart. Lanky is 196 cm tall and Mo is 170 cm tall, so the top of
Mo's head reaches Lanky's chin. Both are fully in frame from head to feet on
the same flat floor. Soft even studio light, shot on a 50mm lens from chest
height of a 175 cm person. Realistic photograph, natural skin texture.
```

## Two-shot prompt template

**Nano Banana Pro:** attach MO_A1, MO_A4, LK_A1, LK_A4, CAST_LINEUP (5 images).
**Nano Banana Flash:** attach MO_A1, LK_A1, CAST_LINEUP (3 images) and change
the first sentence to "Image 1 is Mo's face, image 2 is Lanky's face, image 3
shows both at true height."

```
A vertical 9:16 photograph. Images 1 and 2 are Mo, images 3 and 4 are
Lanky, and image 5 shows them together at their true heights. Keep each man's
face, body, skin, hair and clothing exactly as in his own images, and keep
each man's features entirely his own.

[MO DNA block]

[LK DNA block]

Mo wears [MO wardrobe wording]. Lanky wears [LK wardrobe wording].
Lanky is 196 cm tall and Mo is 170 cm tall, so when they stand side by side
the top of Mo's head reaches Lanky's chin.

[Scene: where and when, in one or two sentences.] Mo is on the left of the
frame and Lanky is on the right. [What each one is doing and their
expressions.]

[Shot size, e.g. medium two-shot with both men's full heads in frame], shot on a 35mm lens at the eye level of a 175 cm person,
[lighting: e.g. cold blue streetlight from the left and warm shop light from
behind]. Unretouched skin with visible pores, fine lines and natural
unevenness. A realistic photograph taken on a full-frame digital camera.
```

Add the location block from `locations/` for the set, and attach that set's
anchor as one more image (or drop LK_A4/MO_A4 on Flash to make room).

Tips:
- Keep the same left/right positions for a whole scene (180° rule). It also
  helps Gemini keep them apart.
- If one face drifts, don't regenerate the whole shot. Edit:
  *"Keep everything in this image exactly the same. Only adjust the face of
  the man on the left so it matches image 1."*
- If heights come out wrong: *"Keep everything the same. Make the man on the
  right taller so the top of the left man's head reaches his chin."* Gemini
  tends to shrink the gap (in the second shoot Mo reached Lanky's eyes, which
  makes Lanky about 182 cm instead of 196 cm). Check it on every standing
  two-shot.
- **Feature bleed:** check each man's eye colour, hair and marks against his
  own bible. In the second shoot Mo came out with Lanky's pale grey-green eyes
  and lost his eyebrow scar. Fix with *"Keep everything the same. Only change
  the left man's eyes to dark brown and add a thin pale scar through the outer
  end of his right eyebrow."*
