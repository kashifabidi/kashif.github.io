#!/usr/bin/env python3
"""Recut the director's 45 s reel as one continuous vlog-camera take.

The director's reel (shots/video/EP01_reel_director_v1.mp4) cuts to Mo
close-ups three times, which made the scene feel shot on different days.
This rebuild keeps the director's pacing, jokes and caption style but
re-renders the whole standing section (0 to 27.5 s of the reel) from our raw
takes, in ONE framing and ONE grade, with no close-ups:

  SH01    director's frames (Mo's intro, Lanky walks in), with the desk and
          laptop composited in from 2b (SH01 was generated without them), then
          a jump cut
  2b+3b   "Is it recording?" (Lanky, head out of frame), Mo looks up, mouths
          "Where's your head?" (2b 107-127, played forward then back so it
          lands on 3b's first frame), mouths "Lower." (3b 0-23)
  3b-4a   director's frames ("Better?", crouch, kneel) with the reel's audio
  4a      "Perfect." while Mo looks down at the kneeling Lanky (his mouth is
          hidden), knee crack on the cut into 4c. "Welcome back to-" is dropped:
          no wide take shows Mo saying it
  4c      director's frames ("Me knees!", topple) with the reel's audio
  4c tail "Fine. We'll do it lying down." over Mo reading his clipboard
          (4c 150-191, then back to 160), then the reel from Cam B onwards

Framing: every Cam A take shares the 2b crop, mapped to the reel's framing
(M_CAMA). SH01 is aligned to 2b on the static room (tripod doesn't move).
Grade: one per-channel tone curve + radial vignette fitted raw->reel.
Captions: Poppins Bold, drop shadow, the reel's size and position.

Run: python3 characters/episodes/recut_reel.py
Out: characters/shots/video/EP01_reel_v2.mp4
"""
import os, subprocess, numpy as np, cv2, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
VID = os.path.join(HERE, "..", "shots", "video")
FONTS = os.path.join(HERE, "..", "assets", "fonts")
FF = imageio_ffmpeg.get_ffmpeg_exe()
REEL = os.path.join(VID, "EP01_reel_director_v1.mp4")
OUT = os.path.join(VID, "EP01_reel_v2.mp4")
W, H, FPS, SR = 1080, 1920, 24, 48000

# raw 720x1280 (2b crop family) -> reel 1080x1920, measured on the reel's 3c/4a/4c
M_CAMA = np.array([[1.8217, 0.0, -72.6071], [0.0, 1.8217, -364.4542]])

# ---------------------------------------------------------------- captions
CAP_Y, CAP_SIZE = 1305, 56
WHITE, YELLOW = (255, 255, 255), (255, 214, 0)
_caps = {}


def caption(text):
    """Reel style. Text in [brackets] is a sound cue: yellow italic."""
    if text in _caps:
        return _caps[text]
    sound = text.startswith("[")
    path = os.path.join(FONTS, "Poppins-BoldItalic.ttf" if sound else "Poppins-Bold.ttf")
    size = CAP_SIZE
    while ImageFont.truetype(path, size).getlength(text) > W - 110:     # keep clear of the edges
        size -= 2
    font = ImageFont.truetype(path, size)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    cx, cy = W // 2, CAP_Y
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            d.text((cx + dx, cy + dy), text, font=font, fill=(0, 0, 0, 255), anchor="mm")
    d.text((cx + 5, cy + 5), text, font=font, fill=(0, 0, 0, 255), anchor="mm")
    d.text((cx, cy), text, font=font, fill=(*(YELLOW if sound else WHITE), 255), anchor="mm")
    a = np.array(img)
    _caps[text] = (a[..., :3][..., ::-1].astype(np.float32), a[..., 3:].astype(np.float32) / 255)
    return _caps[text]


def burn(frame, text):
    rgb, al = caption(text)
    return (frame * (1 - al) + rgb * al).astype(np.uint8)


# ---------------------------------------------------------------- video io
class Clip:
    def __init__(self, path):
        self.v = cv2.VideoCapture(path); self.pos = -1; self.last = (None, None)

    def frame(self, i):
        if self.last[0] == i:
            return self.last[1]
        if i != self.pos + 1:
            self.v.set(1, i)
        ok, f = self.v.read(); self.pos = i
        assert ok, i
        self.last = (i, f)
        return f


_clips = {}


def clip(name):
    if name not in _clips:
        _clips[name] = Clip(REEL if name == "reel" else os.path.join(VID, name))
    return _clips[name]


def orb_fit(a, b):
    """Similarity transform a -> b from ORB matches (RANSAC keeps the static room)."""
    orb = cv2.ORB_create(4000)
    k1, d1 = orb.detectAndCompute(cv2.cvtColor(a, cv2.COLOR_BGR2GRAY), None)
    k2, d2 = orb.detectAndCompute(cv2.cvtColor(b, cv2.COLOR_BGR2GRAY), None)
    m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d1, d2)
    p1 = np.float32([k1[x.queryIdx].pt for x in m]); p2 = np.float32([k2[x.trainIdx].pt for x in m])
    M, _ = cv2.estimateAffinePartial2D(p1, p2, method=cv2.RANSAC, ransacReprojThreshold=2)
    return M


def compose(outer, inner):
    return (np.vstack([outer, [0, 0, 1]]) @ np.vstack([inner, [0, 0, 1]]))[:2]


# ---------------------------------------------------------------- grade
_yy, _xx = np.mgrid[0:H, 0:W].astype(np.float32)
RAD = np.sqrt(((_xx - W / 2) / (W / 2)) ** 2 + ((_yy - H / 2) / (H / 2)) ** 2)


def fit_grade(pairs):
    """Per-channel tone curve (LUT) + radial vignette gain, fitted raw->reel."""
    keep = np.ones((H, W), bool); keep[1240:1370] = False
    keep[:20] = keep[-20:] = False; keep[:, :20] = keep[:, -20:] = False
    A = np.concatenate([cv2.GaussianBlur(a, (0, 0), 1.5)[keep][::7] for a, _ in pairs]).astype(np.float64)
    B = np.concatenate([cv2.GaussianBlur(b, (0, 0), 1.5)[keep][::7] for _, b in pairs]).astype(np.float64)
    R = np.concatenate([RAD[keep][::7] for _ in pairs])
    poly = np.array([0.0]); luts = np.tile(np.arange(256, dtype=np.float64), (3, 1))
    for _ in range(4):
        Bn = B / np.exp(np.polyval(poly, R))[:, None]
        for c in range(3):
            bins = np.clip(A[:, c].astype(int), 0, 255)
            s = np.bincount(bins, Bn[:, c], 256); n = np.bincount(bins, None, 256); have = n > 30
            lut = np.interp(np.arange(256), np.nonzero(have)[0], s[have] / n[have])
            lut = np.convolve(np.pad(lut, 4, mode="edge"), np.ones(9) / 9, "valid")
            luts[c] = np.maximum.accumulate(lut)
        pred = np.stack([luts[c][np.clip(A[:, c].astype(int), 0, 255)] for c in range(3)], 1)
        ratio = np.log(np.clip(B.sum(1), 1, None) / np.clip(pred.sum(1), 1, None))
        rb = np.clip((R / 1.42 * 40).astype(int), 0, 39)
        s = np.bincount(rb, ratio, 40); n = np.bincount(rb, None, 40); ok = n > 50
        poly = np.polyfit(((np.arange(40) + 0.5) / 40 * 1.42)[ok], s[ok] / n[ok], 4)
    return luts.astype(np.float32), np.exp(np.polyval(poly, RAD)).astype(np.float32)


def apply_grade(f, model):
    luts, gain = model
    out = np.stack([luts[c][f[..., c]] for c in range(3)], -1)
    return np.clip(out * gain[..., None], 0, 255).astype(np.uint8)


# ---------------------------------------------------------------- audio
def load_audio(path):
    raw = subprocess.run([FF, "-v", "error", "-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def piece(a, t0, t1, fade=0.03):
    x = a[int(t0 * SR):int(t1 * SR)].copy(); n = max(1, int(fade * SR))
    r = np.linspace(0, 1, n)[:, None]; x[:n] *= r; x[-n:] *= r[::-1]
    return x


def place(buf, x, at, gain=1.0):
    i = int(at * SR); j = min(len(buf), i + len(x))
    buf[i:j] += x[:j - i] * gain


# ---------------------------------------------------------------- the cut
def seq(*parts):
    out = []
    for name, idx in parts:
        out += [(name, i) for i in idx]
    return out


def main():
    reel_a = load_audio(REEL)
    f4b = load_audio(os.path.join(VID, "EP01_SH04b_final.mp4"))
    tone = piece(reel_a, 8.05, 9.45, fade=0.2)                     # the reel's own room tone
    s = lambda frames: frames / FPS

    SH01, B2, B3, C3, A4, C4 = ("EP01_SH01_v1_raw.mp4", "EP01_SH02b_v1_raw.mp4", "EP01_SH03b_v2_raw.mp4",
                                "EP01_SH03c_v1_raw.mp4", "EP01_SH04a_v1_raw.mp4", "EP01_SH04c_v1_raw.mp4")
    geo = {n: M_CAMA for n in (B2, B3, C3, A4, C4)}
    geo[SH01] = compose(M_CAMA, orb_fit(clip(SH01).frame(200), clip(B2).frame(0)))

    # Director's frame sequences (matched frame by frame), so the reel's audio stays in sync.
    # (Where the director flashed 4 frames of 4a's first frame, 3c simply runs on.)
    d_sh01 = [8, 8] + list(range(9, 36)) + list(range(55, 122)) + [122, 124, 124, 126, 127, 128]
    d_3b4a = ([(B3, i) for i in [24, 26, 27, 28, 28] + list(range(29, 52))] +
              [(C3, i) for i in [0, 0] + list(range(1, 24)) + [24, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 36,
                                                              38, 38, 40, 40, 42, 44, 44, 44, 44, 46, 48, 48]] +
              [(C3, i) for i in range(49, 53)] + [(A4, i) for i in [51] + list(range(51, 85))])
    d_4c = [(C4, i) for i in [0, 0, 2, 2, 4, 4, 6, 8, 8] + list(range(9, 150))]

    START_2B = 24
    n_2b = 128 - START_2B + 20                  # 2b forward + back, before 3b starts
    shots = [
        # (frames, audio, captions [(first, last, text)] relative to the shot)
        [seq((SH01, d_sh01)), reel_a[:int(s(102) * SR)],
         [(3, 28, "Welcome back to the chan—"), (37, 101, "[friend enters. mostly.]")]],
        [seq((B2, range(START_2B, 128)), (B2, range(126, 106, -1)), (B3, range(0, 24))), None,
         [(7, 26, "Is it recording?"), (108 - START_2B, 128 - START_2B, "Where's your head?"),
          (n_2b + 4, n_2b + 18, "Lower.")]],
        [d_3b4a, reel_a[int(s(228) * SR):int(s(345) * SR)],
         [(10, 44, "Better?"), (59, 113, "[continues descending]")]],
        [seq((A4, range(85, 121))), None, [(17, 29, "Perfect."), (31, 35, "[crack]")]],
        [d_4c, reel_a[int(s(437) * SR):int(s(587) * SR)], [(6, 66, "[incomprehensible tall-man noises]")]],
        [seq((C4, range(150, 192)), (C4, range(190, 159, -1))), reel_a[int(s(587) * SR):int(s(660) * SR)],
         [(17, 33, "Fine."), (37, 70, "We'll do it lying down.")]],
    ]
    assert len(shots[0][0]) == 102 and len(shots[2][0]) == 117 and len(shots[4][0]) == 150 and len(shots[5][0]) == 73

    # audio for the rebuilt dialogue shots: the reel's room tone + lines
    a2 = np.zeros((int(s(len(shots[1][0])) * SR), 2), np.float32)
    place(a2, np.concatenate([tone] * 8), 0)
    place(a2, piece(reel_a, 4.68, 5.48), s(7))                        # Lanky: "Is it recording?"
    place(a2, piece(reel_a, 6.10, 6.82), s(108 - START_2B))           # Mo: "Where's your head?"
    place(a2, piece(reel_a, 7.50, 8.02), s(n_2b) + 0.22)              # Mo: "Lower."
    n4 = len(shots[3][0]); a4 = np.zeros((int(s(n4) * SR), 2), np.float32)
    place(a4, np.concatenate([tone] * 2), 0)
    place(a4, piece(f4b, 0.18, 0.62), s(104 - 85))                    # Mo: "Perfect."
    place(a4, piece(f4b, 1.36, 1.53, fade=0.005), s(n4) - 0.20, gain=1.6)   # knee crack
    shots[1][1], shots[3][1] = a2, a4

    # one grade for every Cam A frame, fitted on frames the reel shows unchanged
    pairs = []
    for name, i, r in [(B3, 24, 228), (C3, 20, 277), (A4, 84, 344), (C4, 0, 437), (C4, 149, 586)]:
        pairs.append((cv2.warpAffine(clip(name).frame(i), geo[name], (W, H), borderMode=cv2.BORDER_REFLECT),
                      clip("reel").frame(r)))
    model = fit_grade(pairs)
    for a, b in pairs:
        print(f"  grade residual {np.abs(apply_grade(a, model).astype(float) - b).mean():.1f}")

    # The desk and laptop in front of the camera are static, but SH01 was generated
    # without them. Composite them from 2b's first frame onto SH01 so nothing pops in
    # at the jump cut. They're foreground, so covering Lanky's legs is correct.
    desk = apply_grade(cv2.warpAffine(clip(B2).frame(START_2B), geo[B2], (W, H), flags=cv2.INTER_LANCZOS4,
                                      borderMode=cv2.BORDER_REFLECT), model).astype(np.float32)
    mask = np.zeros((H, W), np.float32)
    cv2.fillPoly(mask, [np.array([(0, 1660), (578, 1660), (578, 1250), (590, 1238), (1080, 1238),
                                  (1080, 1920), (0, 1920)], np.int32)], 1.0)
    mask = cv2.GaussianBlur(mask, (0, 0), 2.0)[..., None]

    # audio track (written before the encoder starts reading it)
    audio = [a[:int(s(len(fr)) * SR)] for fr, a, _ in shots] + [reel_a[int(s(660) * SR):]]
    apath = os.path.join(VID, "_reel_audio.f32")
    np.concatenate(audio).astype(np.float32).tofile(apath)

    enc = subprocess.Popen([FF, "-hide_banner", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24",
                            "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-f", "f32le", "-ar", str(SR), "-ac", "2",
                            "-i", apath, "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow",
                            "-b:v", "5000k", "-maxrate", "6000k", "-bufsize", "10000k", "-pix_fmt", "yuv420p",
                            "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
    n = 0
    for frames, _, caps in shots:
        for k, (name, i) in enumerate(frames):
            f = cv2.warpAffine(clip(name).frame(i), geo[name], (W, H), flags=cv2.INTER_LANCZOS4,
                               borderMode=cv2.BORDER_REFLECT)
            f = apply_grade(f, model)
            if name == SH01:
                f = (f * (1 - mask) + desk * mask).astype(np.uint8)
            for a, b, text in caps:
                if a <= k <= b:
                    f = burn(f, text)
            enc.stdin.write(f.tobytes()); n += 1
    for i in range(660, 1080):
        enc.stdin.write(clip("reel").frame(i).tobytes()); n += 1
    enc.stdin.close(); enc.wait(); os.remove(apath)
    print(f"wrote {OUT}: {n} frames ({n / FPS:.2f} s)")


if __name__ == "__main__":
    main()
