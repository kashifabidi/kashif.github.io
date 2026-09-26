# Lanky (code: LK)

**Status:** LOCKED (face)  ·  **Version:** v1.1  ·  **Role:** The tall, wiry one of the duo. Restless, awkward, all elbows.

> Optimised for Gemini. See `../GEMINI.md` for model choice and rules.

## DNA block

> Paste into every Gemini prompt, word for word, even when images are attached.

```
Lanky is a 27-year-old white Irish man, 196 cm tall, very thin and long-limbed
with narrow sloping shoulders and a slight stoop. He has a long narrow face, a
sharp angular jaw, a prominent Adam's apple, a long straight narrow nose, pale
grey-green deep-set eyes and thin light-copper eyebrows. His skin is very pale
and fair, with dense freckles across his nose and cheeks and a faint pink
flush on his ears. His hair is thick, loose, copper-ginger curls, long enough
to cover the tops of his ears and reach his collar at the back, with a few
curls falling onto his forehead. He has a short, uneven light-ginger beard,
thin on the cheeks and fuller on the chin and upper lip. His left ear sticks
out slightly more than his right, one of his lower front teeth is slightly
crooked, and he has a small dark brown mole on the left side of his neck.
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
| Hair | Thick loose copper-ginger curls, covering the tops of his ears, reaching his collar at the back |
| Facial hair | Short uneven ginger beard, thin on cheeks, fuller on chin and upper lip |
| Hands | Long bony fingers, bitten nails |
| Asymmetric anchors | **Left** ear sticks out · crooked lower front tooth · mole **left** side of neck |
| Signature colour | **Teal / petrol blue** |
| Veo tag | "Lanky, the very tall freckled man with curly ginger hair in the teal jacket" |

## Voice (for Veo dialogue)

```
Lanky speaks in a quick, slightly high, nervous voice with a soft Dublin
accent, often trailing off or talking over himself.
```

## Personality → how it looks on camera

- **Resting expression:** slightly worried, brows lifted in the middle.
- **How he stands:** weight on one leg, hands jammed in pockets or rubbing the
  back of his neck.
- **How he moves:** too fast, knocks into things, ducks under door frames.

## Wardrobe

| Code | Outfit (exact wording to paste) |
|---|---|
| LK-W1 (default) | a loose faded teal cotton zip-up jacket with a soft fold-down collar and a full-length front zip, zipped up to mid-chest, over a washed-out white t-shirt, black slim jeans and scuffed white canvas high-top trainers |
| LK-W2 (smart) | an ill-fitting navy suit with sleeves slightly too short, a white shirt and a thin teal tie worn loose |
| LK-W3 (home) | a stretched grey long-sleeve t-shirt, teal pyjama bottoms and bare feet |

## Anchors

From the first Gemini shoot:

| File | What it is |
|---|---|
| `anchors/LK_A1.png` | Head-and-neck crop of the seated shot looking up at Mo. **Face reference only**: neck mole correctly on his **left**. Cropped tight because his jacket in that shot is a half-zip pullover, which is wrong |
| `anchors/LK_A2.png` | Reclined close-up with the can, **after fixing it** (below). Best reference for his hair |

The reclined close-up has the neck mole **mirrored** onto his right side.
His left side isn't visible in that shot, so remove the mole rather than
moving it. Do this before using it as a reference:
```
Keep everything in this image exactly the same. Only remove the small dark
brown moles from the right side of his neck, leaving clear freckled skin.
```
Don't use the short-haired shot (pointing at camera) as a reference: his hair
and face drifted there.

Still needed: **LK_A4** (full body, standing, LK-W1 with the full-length zip).
Run the A4 rebuild prompt below with LK_A1 attached.

## Rebuild prompts (only if starting over)

Run in order, in **one new chat**, on **Nano Banana Pro** if you have it.
Regenerate A1 until it's right before moving on. A1 is the master face.

**A1 front portrait (master face).** 3:4 · save as `anchors/LK_A1.png`
```
A vertical 3:4 studio portrait photograph. Lanky is a 27-year-old white Irish
man, 196 cm tall, very thin and long-limbed with narrow sloping shoulders and
a slight stoop. He has a long narrow face, a sharp angular jaw, a prominent
Adam's apple, a long straight narrow nose, pale grey-green deep-set eyes and
thin light-copper eyebrows. His skin is very pale and fair, with dense
freckles across his nose and cheeks and a faint pink flush on his ears. His
hair is thick, loose, copper-ginger curls, long enough to cover the tops of
his ears and reach his collar at the back, with a few curls falling onto his
forehead. He has a short, uneven light-ginger beard, thin on the cheeks and
fuller on the chin and upper lip. His left ear sticks out slightly more than
his right, one of his lower front teeth is slightly crooked, and he has a
small dark brown mole on the left side of his neck. He wears a loose faded
teal cotton zip-up jacket with a soft fold-down collar and a full-length front
zip, zipped up to mid-chest, over a washed-out white t-shirt.
Head-and-shoulders framing, facing the camera straight on, relaxed neutral
expression with his mouth closed, eyes looking into the lens. Plain mid-grey
seamless studio backdrop, soft even light from a large softbox slightly above
eye level, shot on an 85mm lens at eye level. Unretouched skin with visible
pores, every freckle distinct, fine lines and natural unevenness. A realistic
photograph taken on a full-frame digital camera.
```

**A2 three-quarter.** 3:4 · `LK_A2.png`
```
Keep this exact man: same face, freckles, curly hair, beard, skin tone, marks and
jacket. Turn his head and shoulders three-quarters to his right, so we see
more of the left side of his face, his left ear sticking out and the small
mole on the left side of his neck. Same grey backdrop, same soft light, same
85mm lens, same vertical 3:4 frame. Relaxed neutral expression.
```

**A3 profile.** 3:4 · `LK_A3.png`
```
Keep this exact man. Show his full right-side profile, head and shoulders,
with his long straight nose, prominent Adam's apple and messy ginger hair
falling over his ear clearly visible. Same backdrop, light, lens and 3:4
frame.
```

**A4 full body front.** 9:16 · `LK_A4.png`
```
A vertical 9:16 full-length studio photograph of the same man, keeping his
face, freckles, hair and skin exactly the same. He stands facing the camera
with a slight stoop, weight on one leg, hands pushed into his jacket pockets,
showing his very thin 196 cm frame and long limbs. He wears a loose faded teal
cotton zip-up jacket with a soft fold-down collar and a full-length front zip,
zipped up to mid-chest, over a washed-out white t-shirt, black slim jeans and
scuffed white canvas high-top trainers. Head to trainers fully in frame with a
little space above and below. Same mid-grey seamless backdrop and soft even
light, shot on a 50mm lens from chest height. Realistic photograph, natural
skin texture.
```

**A5 full body side.** 9:16 · `LK_A5.png`
```
Keep this exact man and outfit. He now stands in right-side profile, full
length, with his natural stoop, showing his narrow frame, long legs and
rounded shoulders from the side. Same backdrop, light, 50mm lens and 9:16
frame.
```

**A6 expressions.** 3:4 · `LK_A6a.png`, `LK_A6b.png`, `LK_A6c.png`. One prompt
each, all in the same chat, starting again from A1's framing.
```
Keep this exact man, head-and-shoulders framing as in the first portrait,
same backdrop, light and 85mm lens. He is [a) grinning awkwardly, mouth open
enough to show his slightly crooked lower front tooth | b) panicked, eyes
wide, eyebrows shot up, mouth half open | c) sulking, eyes looking down,
lips pushed out, chin tucked].
```

## Approval checklist

- [ ] Face matches A1 (long narrow face, deep-set pale eyes)
- [ ] Freckles dense and distinct, not smoothed away
- [ ] **Left** ear sticks out, mole on **left** side of neck (Gemini sometimes mirrors these, so check every time)
- [ ] Hair copper-ginger curls covering the tops of his ears and reaching his collar (not short, not cropped)
- [ ] Beard short and uneven, fuller on chin and lip, never a full thick beard
- [ ] Jacket is a full-length front zip (not a half-zip pullover), zipped to mid-chest
- [ ] Wardrobe matches the code exactly
- [ ] Clearly taller and thinner than Mo in two-shots (see CAST.md)
- [ ] Skin has real texture, not plastic smoothing

## Version log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-09-26 | Draft created, optimised for Gemini |
| v1.1 | 2026-09-26 | Hair locked as collar-length loose curls, beard matched to Gemini shoot, jacket locked as full-length zip, Veo tag updated |
