#!/usr/bin/env python3
"""EP01 v3: the one-take cut (see EP01-screenplay-v3.md).

Everything is the vlog camera (Cam A), one afternoon; every cut is a jump cut
inside that take. Reuses the framing, grade, captions and audio helpers from
recut_reel.py (the director's reel supplies the audio for the stretches whose
frames we copy from it).

Run: python3 characters/episodes/build_ep01_v3.py
Out: characters/shots/video/EP01_v3.mp4
"""
import os, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
import recut_reel as R

OUT = os.path.join(R.VID, "EP01_v3.mp4")
R.CAP_Y, R.CAP_SIZE = 1185, 64          # critique: raised off the laptop screen, 15% bigger
M_FULL = np.array([[1.5, 0.0, 0.0], [0.0, 1.5, 0.0]])   # uncropped 720x1280 -> 1080x1920

SH01, B2, B3, C3, A4, C4 = ("EP01_SH01_v1_raw.mp4", "EP01_SH02b_v1_raw.mp4", "EP01_SH03b_v2_raw.mp4",
                            "EP01_SH03c_v1_raw.mp4", "EP01_SH04a_v1_raw.mp4", "EP01_SH04c_v1_raw.mp4")
CA, CB, CC, CD = ("EP01_CT_A_v2_raw.mp4", "EP01_CT_B_raw.mp4", "EP01_CT_C_raw.mp4", "EP01_CT_D_raw.mp4")
s = lambda frames: frames / R.FPS


def bed(tone, dur, xf=0.25):
    """Room tone looped with equal-power crossfades (no dropouts at the joins)."""
    n, x = int(dur * R.SR), int(xf * R.SR)
    out = tone.copy()
    fade = np.sin(np.linspace(0, np.pi / 2, x))[:, None]
    while len(out) < n:
        out = np.concatenate([out[:-x], out[-x:] * fade[::-1] + tone[:x] * fade, tone[x:]])
    return out[:n]


def title_layer(text):
    path, size = os.path.join(R.FONTS, "Poppins-Bold.ttf"), 66
    while ImageFont.truetype(path, size).getlength(text) > R.W - 110:
        size -= 2
    font = ImageFont.truetype(path, size)
    img = Image.new("RGBA", (R.W, R.H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    for dx in range(-3, 4):
        for dy in range(-3, 4):
            d.text((R.W // 2 + dx, 250 + dy), text, font=font, fill=(0, 0, 0, 255), anchor="mm")
    d.text((R.W // 2 + 5, 255), text, font=font, fill=(0, 0, 0, 255), anchor="mm")
    d.text((R.W // 2, 250), text, font=font, fill=(255, 255, 255, 255), anchor="mm")
    a = np.array(img)
    return a[..., :3][..., ::-1].astype(np.float32), a[..., 3:].astype(np.float32) / 255


def main():
    reel_a = R.load_audio(R.REEL)
    f4b = R.load_audio(os.path.join(R.VID, "EP01_SH04b_final.mp4"))
    a5a = R.load_audio(os.path.join(R.VID, "EP01_SH05a_v2_raw.mp4"))
    a1 = R.load_audio(os.path.join(R.VID, "EP01_SH01_v1_raw.mp4"))
    a7a = R.load_audio(os.path.join(R.VID, "EP01_SH07a_v1_raw.mp4"))
    a7b = R.load_audio(os.path.join(R.VID, "EP01_SH07b_v1_raw.mp4"))
    tone = R.piece(reel_a, 8.05, 9.45, fade=0.01)
    reel = lambda a, b: reel_a[int(s(a) * R.SR):int(s(b) * R.SR)]

    geo = {n: R.M_CAMA for n in (B2, B3, C3, A4, C4, CA, CB)}
    geo[SH01] = R.compose(R.M_CAMA, R.orb_fit(R.clip(SH01).frame(200), R.clip(B2).frame(0)))
    geo[CC] = geo[CD] = M_FULL          # punch-out on the jump cut: Mo's walk to the lens

    d_sh01 = [8, 8] + list(range(9, 36)) + list(range(55, 122)) + [122, 124, 124, 126, 127, 128]
    d_3b4a = ([(B3, i) for i in [24, 26, 27, 28, 28] + list(range(29, 52))] +
              [(C3, i) for i in [0, 0] + list(range(1, 24)) + [24, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 36,
                                                              38, 38, 40, 40, 42, 44, 44, 44, 44, 46, 48, 48]] +
              [(C3, i) for i in range(49, 53)] + [(A4, i) for i in [51] + list(range(51, 85))])
    d_4c = [0, 0, 2, 2, 4, 4, 6, 8, 8] + list(range(9, 150))
    J4C = 7                              # enter 4c on the crack, just before "Me knees!"

    shots = []   # [frames [(clip, i)], audio, captions [(first, last, text)]]
    # 1  Intro + jump cut to Lanky half in frame
    shots.append([[(SH01, i) for i in d_sh01[:29]], reel(0, 29), [(3, 28, "Welcome back to the chan—")]])
    shots.append([[(SH01, i) for i in d_sh01[54:102]], reel(54, 102), [(0, 47, "[friend enters. mostly.]")]])
    # 2  "Is it recording?" / look-up / "Where's your head?" / "Lower."
    f = [(B2, i) for i in range(46, 128)] + [(B2, i) for i in range(126, 106, -1)] + [(B3, i) for i in range(24)]
    a = bed(tone, s(len(f)))
    R.place(a, R.piece(reel_a, 4.68, 5.48), s(2))
    R.place(a, R.piece(reel_a, 6.10, 6.82), s(108 - 46))
    R.place(a, R.piece(reel_a, 7.50, 8.02), s(102) + 0.22)
    shots.append([f, a, [(2, 21, "Is it recording?"), (62, 82, "Where's your head?"), (106, 120, "Lower.")]])
    # 3  "Better?" / crouch / kneel (director's frames and audio)
    shots.append([d_3b4a, reel(228, 345), [(10, 44, "Better?"), (59, 113, "[continues descending]")]])
    # 4  "Perfect." (looking down at Lanky), then clip A's own lip-synced intro, cut off by the CRACK
    #    (Veo recorded Mo's lines in clip A; the director's v3 reel showed they work)
    aA = R.load_audio(os.path.join(R.VID, CA))
    f = [(A4, i) for i in range(85, 121)] + [(CA, i) for i in range(0, 124)]
    a = bed(tone, s(len(f)))
    R.place(a, R.piece(f4b, 0.18, 0.62), s(22))                              # "Perfect."
    a[int(s(36) * R.SR):] = 0
    R.place(a, R.piece(aA, 0.0, s(124), fade=0.02), s(36))                   # clip A's own audio
    R.place(a, R.piece(f4b, 1.36, 1.53, fade=0.005), s(len(f)) - 0.12, gain=1.6)  # crack
    shots.append([f, a, [(22, 33, "Perfect."), (36 + 5, 36 + 31, "Welcome back to the channel."),
                         (36 + 43, 36 + 60, "As you can see,"), (36 + 61, 36 + 89, "we've made some major upgrades"),
                         (36 + 94, 36 + 121, "to the studio gear\u2014"), (36 + 122, 36 + 123, "[crack]")]])
    # 5  "Me knees!" / topple (director's frames and audio)
    f = [(C4, i) for i in d_4c[J4C:]]
    shots.append([f, reel(437 + J4C, 587),
                  [(0, 12, "[crack]"), (13, 503 - 437 - J4C, "[incomprehensible tall-man noises]")]])
    # 6  "Fine. We'll do it lying down." over Mo reading his clipboard; ends on clip B's first frame
    f = ([(C4, i) for i in range(150, 192)] + [(C4, i) for i in range(190, 175, -1)] +
         [(C4, i) for i in range(177, 192)] + [(C4, 191)])
    shots.append([f, reel(587, 660), [(17, 33, "Fine."), (37, 70, "We'll do it lying down.")]])
    # 7  Clip B: sigh, lies face down, third intro into the carpet
    f = [(CB, i) for i in range(0, 119)]
    a = bed(tone, s(len(f)))
    R.place(a, R.piece(a5a, 1.15, 1.85), 0.9)                                # sigh
    muff = R.piece(a1, 0.33, 1.40)
    muff = subprocess.run([R.FF, "-v", "error", "-f", "f32le", "-ar", str(R.SR), "-ac", "2", "-i", "-",
                           "-af", "lowpass=f=1800,volume=0.85", "-f", "f32le", "-"],
                          input=muff.astype(np.float32).tobytes(), capture_output=True, check=True).stdout
    R.place(a, np.frombuffer(muff, np.float32).reshape(-1, 2), s(86))
    shots.append([f, a, [(18, 52, "[sighs in content creator]"), (56, 84, "[commits to the bit]"),
                         (86, 114, "Welcome back to the chann—")]])
    # 8  Jump cut: Mo walks to the lens and reads the screen, head bowed (mouth hidden):
    #    "...It's been on landscape." Looks up: clip C's own "You have got to be kidding me."
    aC = R.load_audio(os.path.join(R.VID, CC))
    f = [(CC, i) for i in range(60, 181)]
    a = bed(tone, s(len(f)))
    R.place(a, R.piece(a7a, 0.86, 1.94), s(104 - 60))
    R.place(a, R.piece(aC, 5.50, 6.98), s(132 - 60))
    shots.append([f, a, [(104 - 60, 104 - 60 + 26, "...It's been on landscape."),
                         (137 - 60, 167 - 60, "You have got to be kidding me.")]])
    # 9  Mo's dead stare; Lanky from the floor, off screen. Hard cut back to frame 1.
    f = [(CD, i) for i in range(1, 47)]
    a = bed(tone, s(len(f)))
    R.place(a, R.piece(a7b, 2.86, 3.94), s(4))
    shots.append([f, a, [(4, 30, "So I could have stood up?")]])

    # grade (same fit as reel v2)
    pairs = [(cv2.warpAffine(R.clip(n).frame(i), geo[n], (R.W, R.H), borderMode=cv2.BORDER_REFLECT),
              R.clip("reel").frame(r)) for n, i, r in [(B3, 24, 228), (C3, 20, 277), (A4, 84, 344),
                                                        (C4, 0, 437), (C4, 149, 586)]]
    model = R.fit_grade(pairs)
    desk = R.apply_grade(cv2.warpAffine(R.clip(B2).frame(46), geo[B2], (R.W, R.H), flags=cv2.INTER_LANCZOS4,
                                        borderMode=cv2.BORDER_REFLECT), model).astype(np.float32)
    mask = np.zeros((R.H, R.W), np.float32)
    cv2.fillPoly(mask, [np.array([(0, 1660), (578, 1660), (578, 1250), (590, 1238), (1080, 1238),
                                  (1080, 1920), (0, 1920)], np.int32)], 1.0)
    mask = cv2.GaussianBlur(mask, (0, 0), 2.0)[..., None]
    title = title_layer("Filming Shorts with a 6'5\" mate")

    apath = os.path.join(R.VID, "_v3_audio.f32")
    np.concatenate([a[:int(s(len(f)) * R.SR)] for f, a, _ in shots]).astype(np.float32).tofile(apath)
    enc = subprocess.Popen([R.FF, "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24",
                            "-s", f"{R.W}x{R.H}", "-r", str(R.FPS), "-i", "-", "-f", "f32le", "-ar", str(R.SR),
                            "-ac", "2", "-i", apath, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow",
                            "-b:v", "5000k", "-maxrate", "6000k", "-bufsize", "10000k", "-pix_fmt", "yuv420p",
                            "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k",
                            "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
    n = 0
    for frames, _, caps in shots:
        for k, (name, i) in enumerate(frames):
            fr = cv2.warpAffine(R.clip(name).frame(i), geo[name], (R.W, R.H), flags=cv2.INTER_LANCZOS4,
                                borderMode=cv2.BORDER_REFLECT)
            fr = R.apply_grade(fr, model)
            if name == SH01:
                fr = (fr * (1 - mask) + desk * mask).astype(np.uint8)
            if n < 48:
                rgb, al = title; fr = (fr * (1 - al) + rgb * al).astype(np.uint8)
            for a, b, text in caps:
                if a <= k <= b:
                    fr = R.burn(fr, text)
            enc.stdin.write(fr.tobytes()); n += 1
    enc.stdin.close(); enc.wait(); os.remove(apath)
    print(f"wrote {OUT}: {n} frames ({n / R.FPS:.2f} s); shot starts:",
          np.cumsum([0] + [len(f) for f, _, _ in shots])[:-1].tolist())


if __name__ == "__main__":
    main()
