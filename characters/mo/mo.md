# Mo (code: MO)

**Status:** DRAFT  ·  **Version:** v1  ·  **Role:** The short, solid one of the duo. Grounded, warm, quick with a look.

> ⚠️ Draft defaults. Everything below is a starting suggestion. Change any
> trait **before** you generate A1, then lock it.
>
> Optimised for Gemini. See `../GEMINI.md` for model choice and rules.

## DNA block

> Paste into every Gemini prompt, word for word, even when images are attached.

```
Mo is a 32-year-old British-Pakistani man, 170 cm tall, solidly built and
soft around the middle, with rounded shoulders and a slight belly. He has a
round, open face with full cheeks, a soft rounded jaw, a broad nose, and warm
dark brown eyes with gentle laughter lines at the corners. His eyebrows are
thick, black and softly arched. His skin is warm medium-brown with natural
texture and faint shadows under the eyes. His black hair is short and neat,
slightly wavy on top and combed loosely to one side. He has a short, neatly
trimmed black beard with a few grey hairs on the left side of his chin. He
has a small mole on his right cheekbone and a slight gap between his two
front teeth. His face at rest has a relaxed, friendly look, as if he is about
to smile.
```

## Physical spec

| Trait | Value |
|---|---|
| Age | 32 |
| Height / weight | 170 cm / ~85 kg |
| Build / posture | Solid and soft-bodied, rounded shoulders, slight belly; stands relaxed, feet planted |
| Face shape | Round, open, full cheeks, soft rounded jaw |
| Eyes | Warm dark brown, gentle laughter lines |
| Skin | Warm medium-brown, natural texture |
| Hair | Black, short and neat, slightly wavy on top, combed loosely to one side |
| Facial hair | Short neat black beard, a few grey hairs on the left of the chin |
| Hands | Broad, short fingers, silver ring on right index finger |
| Asymmetric anchors | Mole **right** cheekbone · grey hairs **left** of chin · gap in front teeth |
| Signature colour | **Mustard / ochre** |
| Veo tag | "Mo, the short bearded man in the mustard jacket" |

## Voice (for Veo dialogue)

```
Mo speaks in a low, warm, unhurried voice with a Birmingham accent, dry and
deadpan, rarely raising his volume.
```

## Personality → how it looks on camera

- **Resting expression:** relaxed and friendly, a faint half-smile, like he's
  already heard the excuse and finds it funny.
- **How he stands:** relaxed, hands in jacket pockets or holding a mug.
- **How he moves:** economical, unhurried, turns his whole body rather than
  just his head.

## Wardrobe

| Code | Outfit (exact wording to paste) |
|---|---|
| MO-W1 (default) | a mustard-yellow waxed cotton work jacket over a plain charcoal crew-neck t-shirt, dark indigo straight-leg jeans and brown leather work boots |
| MO-W2 (smart) | a charcoal wool overcoat over a black roll-neck jumper, dark grey trousers and black leather shoes |
| MO-W3 (home) | a faded mustard hoodie, grey joggers and black slides |

## Anchor prompts

Run in order, in **one new chat**, on **Nano Banana Pro** if you have it.
Regenerate A1 until it's right before moving on. A1 is the master face.

**A1 front portrait (master face).** 3:4 · save as `anchors/MO_A1.png`
```
A vertical 3:4 studio portrait photograph. Mo is a 32-year-old
British-Pakistani man, 170 cm tall, solidly built and soft around the middle,
with rounded shoulders and a slight belly. He has a round, open face with full
cheeks, a soft rounded jaw, a broad nose, and warm dark brown eyes with gentle
laughter lines at the corners. His eyebrows are thick, black and softly
arched. His skin is warm medium-brown with natural texture and faint shadows
under the eyes. His black hair is short and neat, slightly wavy on top and
combed loosely to one side. He has a short, neatly trimmed black beard with a
few grey hairs on the left side of his chin. He has a small mole on his right
cheekbone and a slight gap between his two front teeth. His face at rest has a
relaxed, friendly look, as if he is about to smile. He wears a mustard-yellow
waxed cotton work jacket over a plain charcoal crew-neck t-shirt.
Head-and-shoulders framing, facing the camera straight on, relaxed friendly
expression with a faint closed-mouth half-smile and soft eyes, looking into
the lens. Plain mid-grey seamless studio backdrop, soft warm even light from a
large softbox slightly above eye level, shot on an 85mm lens at eye level.
Unretouched skin with visible pores, fine lines and natural unevenness. A
realistic photograph taken on a full-frame digital camera.
```

**A2 three-quarter.** 3:4 · `MO_A2.png`
```
Keep this exact man: same face, beard, hair, skin tone, marks and jacket.
Turn his head and shoulders three-quarters to his right, so we see more of
the left side of his face and the few grey hairs on the left side of his
chin. Same grey backdrop, same soft light, same 85mm lens, same
vertical 3:4 frame. Relaxed friendly expression.
```

**A3 profile.** 3:4 · `MO_A3.png`
```
Keep this exact man. Show his full right-side profile, head and shoulders,
with the small mole on his right cheekbone visible and the shape of his
broad nose clear. Same backdrop, light, lens and 3:4 frame.
```

**A4 full body front.** 9:16 · `MO_A4.png`
```
A vertical 9:16 full-length studio photograph of the same man, keeping his
face, beard, hair and skin exactly the same. He stands facing the camera,
feet planted, arms relaxed at his sides, showing his solid 170 cm frame and
slight belly. He wears a mustard-yellow waxed cotton work jacket over a plain
charcoal crew-neck t-shirt, dark indigo straight-leg jeans and brown leather
work boots, with a silver ring on his right index finger. Head to boots fully
in frame with a little space above and below. Same mid-grey seamless backdrop
and soft even light, shot on a 50mm lens from chest height. Realistic
photograph, natural skin texture.
```

**A5 full body side.** 9:16 · `MO_A5.png`
```
Keep this exact man and outfit. He now stands in right-side profile, full
length, natural relaxed posture, showing his rounded shoulders, solid build
and slight belly from the side. Same backdrop, light, 50mm lens and 9:16
frame.
```

**A6 expressions.** 3:4 · `MO_A6a.png`, `MO_A6b.png`, `MO_A6c.png`. One prompt
each, all in the same chat, starting again from A1's framing.
```
Keep this exact man, head-and-shoulders framing as in the first portrait,
same backdrop, light and 85mm lens. He is [a) laughing genuinely, eyes
creased, mouth open so the gap between his front teeth shows |
b) skeptical, one eyebrow raised, lips pressed together, head tilted slightly
back | c) angry, jaw clenched, brows pulled down, nostrils flared].
```

## Approval checklist

- [ ] Face matches A1 (round open face, soft jaw, warm eyes with laughter lines)
- [ ] Mole on **right** cheekbone, grey beard hairs on **left** of chin (Gemini sometimes mirrors these, so check every time)
- [ ] Tooth gap visible when smiling
- [ ] Skin tone warm medium-brown, not lightened by the lighting
- [ ] Beard short and neat, not stubble, not long or bushy
- [ ] Reads friendly and approachable, not tough
- [ ] Wardrobe matches the code exactly
- [ ] Clearly shorter than Lanky in two-shots (see CAST.md)
- [ ] Skin has real texture, not plastic smoothing

## Version log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-09-26 | Draft created, optimised for Gemini |
| v1.1 | 2026-09-26 | Softened: rounder jaw, warm eyes, neat hair, scar replaced by grey beard hairs, friendly resting look |
