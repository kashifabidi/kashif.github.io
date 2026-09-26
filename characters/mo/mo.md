# Mo (code: MO)

**Status:** DRAFT  ·  **Version:** v1  ·  **Role:** The short, solid one of the duo. Grounded, warm, quick with a look.

> ⚠️ Draft defaults. Everything below is a starting suggestion. Change any
> trait **before** you generate A1, then lock it.

## DNA block

> Paste into every prompt, word for word. Never paraphrase.

```
Mo: a 32-year-old British-Pakistani man, 5 ft 7 in (170 cm) tall, stocky and
broad-shouldered with a slight belly. Round face with full cheeks, strong
short jaw, broad slightly hooked nose, dark brown almond-shaped eyes with
heavy lids, thick straight black eyebrows. Warm medium-brown skin with
natural texture and faint under-eye shadows. Short black hair, tight fade on
the sides, slightly longer on top pushed forward. Full, neatly trimmed short
black beard. Distinguishing marks: small mole on his right cheekbone, a thin
pale scar through the outer end of his left eyebrow, slight gap between his
two front teeth.
```

## Physical spec

| Trait | Value |
|---|---|
| Age | 32 |
| Height / weight | 170 cm / ~85 kg |
| Build / posture | Stocky, broad, low centre of gravity; stands square, feet planted |
| Face shape | Round, full cheeks, short strong jaw |
| Eyes | Dark brown, almond, heavy-lidded |
| Skin | Warm medium-brown, natural texture |
| Hair | Black, short fade, longer on top pushed forward |
| Facial hair | Full short trimmed black beard |
| Hands | Broad, short fingers, silver ring on right index finger |
| Asymmetric anchors | Mole **right** cheekbone · scar through **left** eyebrow · gap in front teeth |
| Signature colour | **Mustard / ochre** |

## Personality → how it looks on camera

- **Resting expression:** half-smile, one eyebrow slightly raised, like he's
  already heard the excuse.
- **How he stands:** square, arms folded or hands in jacket pockets.
- **How he moves:** economical, unhurried, turns his whole body rather than
  just his head.

## Wardrobe

| Code | Outfit (exact wording to paste) |
|---|---|
| MO-W1 (default) | mustard-yellow waxed cotton work jacket over a plain charcoal crew-neck t-shirt, dark indigo straight jeans, brown leather work boots |
| MO-W2 (smart) | charcoal wool overcoat over a black roll-neck jumper, dark grey trousers, black leather shoes |
| MO-W3 (home) | faded mustard hoodie, grey joggers, black slides |

## Anchor prompts (run in order, same Gemini chat)

**A1 front portrait (master face).** Save as `anchors/MO_A1.png`.
```
Photograph of Mo: [DNA block]. Wearing MO-W1: mustard-yellow waxed cotton work
jacket over a plain charcoal crew-neck t-shirt. Head and shoulders, facing the
camera straight on, neutral expression, mouth closed. Plain mid-grey studio
backdrop, soft even key light, 85mm lens, eye level. Real skin texture,
visible pores, natural asymmetry, no retouching, no beauty filter.
Photographed, not rendered.
```

**A2 three-quarter.** `MO_A2.png`
```
Same person as the previous image, identical face and features. Head and
shoulders, turned three-quarters to his right so we see the left side of his
face and the scar through his left eyebrow. Same backdrop, light and lens.
Neutral expression.
```

**A3 profile.** `MO_A3.png`
```
Same person, identical face. Full right-side profile, head and shoulders,
showing the mole on his right cheekbone. Same backdrop, light and lens.
```

**A4 full body front.** `MO_A4.png`
```
Same person, identical face. Full body head to toe, standing square facing
camera, arms relaxed, wearing MO-W1: mustard-yellow waxed cotton work jacket
over a plain charcoal crew-neck t-shirt, dark indigo straight jeans, brown
leather work boots. He is 170 cm tall and stocky. Same grey backdrop, 50mm
lens, camera at chest height.
```

**A5 full body side.** `MO_A5.png`
```
Same person, same outfit, full body, standing in right-side profile, natural
posture showing his stocky build and slight belly. Same backdrop, 50mm lens.
```

**A6 expressions.** `MO_A6a.png` … `MO_A6c.png` (one prompt each, not a grid)
```
Same person, identical face, head and shoulders, same backdrop and 85mm lens.
Expression: [a) genuine laugh showing the gap in his front teeth |
b) skeptical, one eyebrow raised, lips pressed | c) angry, jaw clenched,
brows down].
```

## Approval checklist

- [ ] Face matches A1 (round face, hooked nose, heavy-lidded eyes)
- [ ] Mole on **right** cheekbone, scar through **left** eyebrow
- [ ] Tooth gap visible when smiling
- [ ] Skin tone matches: warm medium-brown, not lightened
- [ ] Beard full and short, not stubble, not long
- [ ] Wardrobe matches code exactly
- [ ] Looks clearly shorter than Lanky in two-shots (see CAST.md)
- [ ] No "AI face" smoothing

## Version log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-09-26 | Draft created |
