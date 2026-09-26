# The Studio (code: STU)

**Status:** DRAFT  ·  **Version:** v1  ·  Mo and Lanky's home content-creator studio.

Sets drift like faces do: in the first shoot the ring light, shelves and
window moved between shots. Treat the room like a character: one fixed
description, pasted word for word, plus anchor images attached to every shot
here.

## Set block

> Paste into every prompt set in the studio, word for word.

```
The studio is a bright converted living room with white walls and a pale grey
carpet. On the left, a tall window with sheer white curtains lets in soft
daylight. Against the back wall stands a grey fabric three-seater sofa. Behind
the sofa, two beige fabric acoustic panels lean against the wall, with a black
acoustic foam panel mounted high above them. On the right, white floating
shelves hold camera bodies and lenses, and below them a light wooden desk
holds a monitor showing a video editing timeline. Two cameras on black
tripods stand to the left of the sofa, and a ring light on a black stand with
a microphone on a boom arm stands between the sofa and the desk.
```

## Layout (keep consistent)

| Area | What's there |
|---|---|
| Left | Tall window, sheer white curtains; two cameras on tripods in front of it |
| Centre | Grey three-seater sofa against the back wall; beige acoustic panels behind; black foam panel above |
| Right | White floating shelves with cameras and lenses; wooden desk with monitor below |
| Between sofa and desk | Ring light on a black stand, microphone on a boom arm |
| Light | Soft daylight from the left window, warm fill from the ring light |

Keep this layout fixed. If a shot looks the other way, describe what's
behind the camera instead of moving things.

## Screens

The monitor always shows **a video editing timeline with no people on
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
