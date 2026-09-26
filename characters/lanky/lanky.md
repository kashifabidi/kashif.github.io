# Lanky (code: LK)

**Status:** DRAFT  ·  **Version:** v1  ·  **Role:** The tall, wiry one of the duo. Restless, awkward, all elbows.

> ⚠️ Draft defaults. Everything below is a starting suggestion. Change any
> trait **before** you generate A1, then lock it.

## DNA block

> Paste into every prompt, word for word. Never paraphrase.

```
Lanky: a 27-year-old white Irish man, 6 ft 5 in (196 cm) tall, very thin and
long-limbed with narrow sloping shoulders and a slight stoop. Long narrow face,
sharp angular jaw, prominent Adam's apple, long straight narrow nose, pale
grey-green deep-set eyes, thin light-copper eyebrows. Very pale fair skin with
dense freckles across the nose and cheeks and a faint pink flush on the ears.
Messy medium-length copper-ginger hair, wavy, falling over his forehead and
ears. Patchy light ginger stubble. Distinguishing marks: left ear sticks out
slightly more than the right, small crooked lower front tooth, a dark brown
mole on the left side of his neck.
```

## Physical spec

| Trait | Value |
|---|---|
| Age | 27 |
| Height / weight | 196 cm / ~72 kg |
| Build / posture | Very thin, long limbs, narrow sloped shoulders, slight stoop, hunches to talk to people |
| Face shape | Long, narrow, angular |
| Eyes | Pale grey-green, deep-set |
| Skin | Very pale, heavy freckles, pink ears |
| Hair | Copper-ginger, wavy, medium length, messy, over forehead |
| Facial hair | Patchy light ginger stubble |
| Hands | Long bony fingers, bitten nails |
| Asymmetric anchors | **Left** ear sticks out · crooked lower front tooth · mole **left** side of neck |
| Signature colour | **Teal / petrol blue** |

## Personality → how it looks on camera

- **Resting expression:** slightly worried, brows lifted in the middle.
- **How he stands:** weight on one leg, hands jammed in pockets or rubbing the
  back of his neck.
- **How he moves:** too fast, knocks into things, ducks under door frames.

## Wardrobe

| Code | Outfit (exact wording to paste) |
|---|---|
| LK-W1 (default) | oversized faded teal zip-up track jacket, over a washed-out white t-shirt, black skinny jeans too short at the ankle, scuffed white canvas high-top trainers |
| LK-W2 (smart) | ill-fitting navy suit with sleeves slightly too short, white shirt, thin teal tie loosened |
| LK-W3 (home) | stretched grey long-sleeve t-shirt, teal pyjama bottoms, bare feet |

## Anchor prompts (run in order, same Gemini chat)

**A1 front portrait (master face).** Save as `anchors/LK_A1.png`.
```
Photograph of Lanky: [DNA block]. Wearing LK-W1: oversized faded teal zip-up
track jacket over a washed-out white t-shirt. Head and shoulders, facing the
camera straight on, neutral expression, mouth closed. Plain mid-grey studio
backdrop, soft even key light, 85mm lens, eye level. Real skin texture,
visible pores and freckles, natural asymmetry, no retouching, no beauty filter.
Photographed, not rendered.
```

**A2 three-quarter.** `LK_A2.png`
```
Same person as the previous image, identical face and features. Head and
shoulders, turned three-quarters to his right so we see the left side of his
face, his protruding left ear and the mole on the left side of his neck. Same
backdrop, light and lens. Neutral expression.
```

**A3 profile.** `LK_A3.png`
```
Same person, identical face. Full right-side profile, head and shoulders,
showing his long straight nose, prominent Adam's apple and messy ginger hair.
Same backdrop, light and lens.
```

**A4 full body front.** `LK_A4.png`
```
Same person, identical face. Full body head to toe, standing facing camera
with a slight stoop, weight on one leg, hands in jacket pockets, wearing
LK-W1: oversized faded teal zip-up track jacket over a washed-out white
t-shirt, black skinny jeans too short at the ankle, scuffed white canvas
high-top trainers. He is 196 cm tall and very thin with long limbs. Same grey
backdrop, 50mm lens, camera at chest height.
```

**A5 full body side.** `LK_A5.png`
```
Same person, same outfit, full body, standing in right-side profile, showing
his stoop, narrow frame and long legs. Same backdrop, 50mm lens.
```

**A6 expressions.** `LK_A6a.png` … `LK_A6c.png` (one prompt each, not a grid)
```
Same person, identical face, head and shoulders, same backdrop and 85mm lens.
Expression: [a) awkward grin showing the crooked lower tooth |
b) panicked, eyes wide, brows up | c) sulking, looking down, lips pushed out].
```

## Approval checklist

- [ ] Face matches A1 (long narrow face, deep-set pale eyes)
- [ ] Freckles dense and present, not airbrushed away
- [ ] **Left** ear sticks out, mole on **left** side of neck
- [ ] Hair copper-ginger, not brown, not bright orange
- [ ] Stubble patchy, not a full beard
- [ ] Wardrobe matches code exactly
- [ ] Clearly taller and thinner than Mo in two-shots (see CAST.md)
- [ ] No "AI face" smoothing

## Version log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-09-26 | Draft created |
