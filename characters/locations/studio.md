# The Studio (code: STU)

**Status:** LOCKED (Cam A)  ·  **Version:** v2  ·  Mo and Lanky's home content-creator studio.

Sets drift like faces do: in the first shoot the ring light, shelves and
window moved between shots. Treat the room like a character: one fixed
description, pasted word for word, plus anchor images attached to every shot
here.

## Set block

> Paste into every prompt set in the studio, word for word.

```
The studio is a small, bright converted living room with white walls and a
pale grey carpet. On the left, a tall window with sheer white curtains lets
in soft daylight, and two cameras on black tripods stand in front of it.
Against the back wall stands a grey fabric three-seater sofa with light
wooden legs. Behind the sofa, two beige fabric acoustic panels lean against
the wall, with a square black acoustic foam panel mounted high above them. A
ring light on a black stand and a microphone on a black boom arm stand
between the sofa and the desk. On the right, white floating shelves hold
camera lenses and two small plants, and below them a light wooden standing
desk holds an open laptop showing a video editing timeline.
```

## Camera positions

The room is small, so every shot comes from one of these fixed positions.
Each gets its own empty-room anchor, made when first needed.

| Camera | Position | Anchor |
|---|---|---|
| **Cam A** | Tripod in the middle of the room at chest height, facing the sofa (the "vlog camera") | `anchors/STU_A2.png` ✅ |
| **Cam B** | High in the front-right corner by the ring light, looking down across the carpet | `anchors/STU_B.png` ⏳ |
| **Cam C** | Straight overhead, looking down at the carpet in front of the sofa | `anchors/STU_C.png` ⏳ |
| **Cam D** | Reverse angle from the sofa, facing the window and the two tripods | `anchors/STU_D.png` ⏳ |

## Layout (keep consistent)

| Area | What's there |
|---|---|
| Left | Tall window, sheer white curtains; two cameras on tripods in front of it |
| Centre | Grey three-seater sofa against the back wall; beige acoustic panels behind; black foam panel above |
| Right | White floating shelves with lenses and two small plants; light wooden standing desk with an open laptop below |
| Between sofa and desk | Ring light on a black stand, microphone on a boom arm |
| Light | Soft daylight from the left window, warm fill from the ring light |

Keep this layout fixed. If a shot looks the other way, describe what's
behind the camera instead of moving things.

## Screens

The laptop always shows **a video editing timeline with no people on
screen**, unless a scene says otherwise. Always state it in the Veo prompt.

## Props

| Prop | Owner | Exact wording |
|---|---|---|
| Clipboard | Mo | a brown hardboard clipboard with a silver clip, holding a handwritten page |
| Can | Lanky | a plain silver drinks can with no label |

To show the clipboard's writing, give it the exact text, e.g. *"the page reads
'SHOOT PLAN' in black marker, with three short lines underneath"*. Otherwise
write *"the clipboard faces away from camera"* so Gemini doesn't render
unreadable scribble.

## Anchors

Make these once, in a new Gemini chat, with no people, and save to
`locations/anchors/`:

**STU_A1 wide (16:9 reference).**
```
A horizontal 16:9 photograph of an empty room, no people. [Set block]
Shot from the middle of the room facing the sofa, 24mm lens at chest height,
soft natural daylight. A realistic photograph taken on a full-frame digital
camera.
```

**STU_A2 vertical (9:16 reference).**
```
Same room, same furniture in the same places. A vertical 9:16 photograph
facing the sofa, 35mm lens at chest height, no people.
```

Attach STU_A1 or STU_A2 to every shot in the studio. It uses one reference
slot, so on Flash drop the characters' A4 images to make room.

## Version log

| Version | Date | Change |
|---|---|---|
| v1 | 2026-09-26 | Created from the first Gemini shoot |
