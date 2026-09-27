#!/usr/bin/env python3
"""Continuity finishing pass for EP01.

Makes the rough cut read as one continuous take from two cameras:
  1. Per-clip colour match in LAB (remove each generation's cast/exposure).
  2. Per-clip texture match (tame over-sharp clips, lift soft ones).
  3. One shared "camera" look on top: gentle curve, vignette, film grain.
  4. One soundscape: per-clip denoise + band-limit, 15 ms edge fades, and a
     continuous room-tone bed under the whole timeline.

Run from anywhere:  python3 characters/episodes/finish_ep01.py
Output: characters/shots/video/EP01_finished.mp4
"""
import os, re, subprocess, cv2, numpy as np, imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__))
VID = os.path.join(HERE, "..", "shots", "video")
TMP = os.path.join(VID, "_finish")
FF = imageio_ffmpeg.get_ffmpeg_exe()
os.makedirs(TMP, exist_ok=True)

CLIPS = re.search(r"CLIPS=\(([^)]*)\)", open(os.path.join(HERE, "assemble_ep01.sh")).read()).group(1).split()

# Target look: the approved Cam A hero clip (2a) for colour, a common texture level.
TARGET_A, TARGET_B = 2.8, 5.5          # neutral with a touch of warmth (LAB a/b, centred)
TARGET_L = 122.0                        # overall exposure target
L_STRENGTH = 0.5                        # move exposure 60% toward target (keeps real light changes)
TARGET_SHARP = 140.0                    # Laplacian variance to aim for


def stats(path):
    v = cv2.VideoCapture(path); n = int(v.get(7)); L = []; S = []
    for i in np.linspace(0, n - 1, 10).astype(int):
        v.set(1, i); ok, f = v.read()
        if not ok: continue
        lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).reshape(-1, 3).astype(float)
        L.append(lab.mean(0))
        S.append(cv2.Laplacian(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY), cv2.CV_64F).var())
    return np.mean(L, 0), float(np.mean(S))


def grade_clip(name):
    src = os.path.join(VID, name + ".mp4")
    m, sharp = stats(src)
    dL = float(np.clip((TARGET_L - m[0]) * L_STRENGTH, -10, 8))
    da = (128 + TARGET_A) - m[1]
    db = (128 + TARGET_B) - m[2]
    # texture: blur if too sharp, unsharp if too soft
    ratio = sharp / TARGET_SHARP
    sigma = float(np.clip(0.55 * np.log2(ratio), 0, 1.6)) if ratio > 1.3 else 0.0
    amount = float(np.clip(0.45 * np.log2(1 / ratio), 0, 0.9)) if ratio < 0.7 else 0.0

    v = cv2.VideoCapture(src)
    w, h = int(v.get(3)), int(v.get(4))
    out_v = os.path.join(TMP, name + "_v.mp4")
    wr = cv2.VideoWriter(out_v, cv2.VideoWriter_fourcc(*"mp4v"), 24, (w, h))
    while True:
        ok, f = v.read()
        if not ok: break
        lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
        lab[..., 0] += dL; lab[..., 1] += da; lab[..., 2] += db
        f = cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
        if sigma > 0:
            f = cv2.GaussianBlur(f, (0, 0), sigma)
        if amount > 0:
            bl = cv2.GaussianBlur(f, (0, 0), 1.2)
            f = cv2.addWeighted(f, 1 + amount, bl, -amount, 0)
        wr.write(f)
    wr.release()

    # audio: denoise to a common floor, band-limit, soft edges; mux with graded picture
    dur = float(v.get(7)) / 24.0
    out = os.path.join(TMP, name + ".mp4")
    af = (f"aresample=48000,aformat=channel_layouts=stereo,highpass=f=80,lowpass=f=11000,"
          f"afftdn=nr=12:nf=-50,afade=t=in:d=0.015,afade=t=out:st={max(0, dur - 0.015):.3f}:d=0.015,apad")
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", out_v, "-i", src,
                    "-map", "0:v", "-map", "1:a", "-af", af, "-c:v", "libx264", "-crf", "14",
                    "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "pcm_s16le",
                    "-shortest", out.replace(".mp4", ".mov")], check=True)
    print(f"{name:22s} dL{dL:+6.1f} da{da:+5.1f} db{db:+5.1f} sharp{sharp:7.0f} blur{sigma:.2f} unsharp{amount:.2f}")
    return out.replace(".mp4", ".mov")


def main():
    parts = [grade_clip(c) for c in CLIPS]

    # concatenate
    lst = os.path.join(TMP, "list.txt")
    with open(lst, "w") as fh:
        for p in parts: fh.write(f"file '{p}'\n")
    joined = os.path.join(TMP, "joined.mov")
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", joined], check=True)

    # room-tone bed: loop the quiet look-up clip (2b) under everything
    bed_src = os.path.join(VID, "EP01_SH02b_final.mp4")
    look = ("curves=all='0/0 0.06/0.045 0.5/0.52 0.94/0.96 1/1',"
            "vignette=angle=PI/9,noise=alls=5:allf=t,format=yuv420p")
    out = os.path.join(VID, "EP01_finished.mp4")
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", joined,
                    "-stream_loop", "-1", "-i", bed_src,
                    "-filter_complex",
                    f"[0:v]{look}[v];"
                    "[1:a]aresample=48000,aformat=channel_layouts=stereo,highpass=f=80,lowpass=f=6000,volume=0.6[bed];"
                    "[0:a][bed]amix=inputs=2:duration=first:normalize=0,"
                    "loudnorm=I=-16:TP=-1.5:LRA=9[a]",
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "17", "-preset", "slow",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
    print("wrote", out)


if __name__ == "__main__":
    main()
