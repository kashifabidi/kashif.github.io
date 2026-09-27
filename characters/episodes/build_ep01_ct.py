#!/usr/bin/env python3
"""Build the EP01 continuity clips (single camera, Cam A) from raw takes.

Each clip is a list of picture parts (raw file, frame range, optional reverse)
cropped with the 2b box, plus approved dialogue laid in over room tone.
Forward-then-reverse ("ping-pong") parts are only used on near-static
stretches, so a clip can start and end on the exact frames its neighbours use.

Run: python3 characters/episodes/build_ep01_ct.py
Writes characters/shots/video/EP01_CT*_final.mp4 (720x1280, 24 fps).
"""
import os, subprocess, imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__))
VID = os.path.join(HERE, "..", "shots", "video")
FF = imageio_ffmpeg.get_ffmpeg_exe()
UP = os.environ.get("EP01_UPLOADS", os.path.join(VID, "_ct_src"))

BOX_2B = (41, 200, 592, 1054)          # x, y, w, h: shared crop for all Cam A wides
ROOM = "EP01_SH02b_final.mp4"          # room tone source (silent look-up)

CLIP_A = "EP01_CT_A_v2_raw.mp4"        # Veo: first = last = EP01_SH04c_first_frame.png
                                       # (v1 was made from the wrong frame: Lanky on the floor)
CLIP_B = "EP01_CT_B_raw.mp4"           # Veo: first = EP01_CT_B_first_frame.png

# name: (picture parts [(file, first_frame, last_frame_inclusive, reverse)],
#        lines [(file, t0, t1, at, muffled)])
CLIPS = {
    # Beat 4 - Mo: "Where's your head?" 2b raw tail (Mo mouths it), then back to
    # frame 106, which is 3b v2's first frame.
    "EP01_CT04_final": (
        [("EP01_SH02b_v1_raw.mp4", 107, 127, False), ("EP01_SH02b_v1_raw.mp4", 107, 126, True)],
        [("EP01_SH02c_v2_raw.mp4", 2.80, 3.58, 0.08, False)]),
    # Beat 5 - Mo: "Lower." 3b v2 up to the frame 3b_final starts on.
    "EP01_CT05_final": (
        [("EP01_SH03b_v2_raw.mp4", 0, 23, False)],
        [("EP01_SH03a_final.mp4", 0.50, 1.02, 0.22, False)]),
    # Beat 8 - Mo reads his clipboard: "Perfect. Welcome back to-" + crack + gasp.
    # Clip A's still tail, played back then forward: starts on 4a_final's last
    # frame and ends on 4c's first frame.
    "EP01_CT08_final": (
        [(CLIP_A, 162, 184, True), (CLIP_A, 163, 191, False)],
        [("EP01_SH04b_final.mp4", 0.0, 2.17, 0.0, False)]),
    # Beats 10-11 - "Fine. We'll do it lying down." over 4c's tail, then clip B:
    # Mo lies face down and starts the intro into the carpet.
    "EP01_CT10_final": (
        [("EP01_SH04c_v1_fixed.mp4", 156, 191, False), (CLIP_B, 0, 155, False)],
        [("EP01_SH05a_v2_raw.mp4", 3.15, 5.40, 0.15, False),
         ("EP01_SH01_v1_raw.mp4", 0.33, 1.40, 5.10, True)]),
}


def src(f):
    p = os.path.join(VID, f)
    return p if os.path.exists(p) else os.path.join(UP, f)


def build(name, parts, lines):
    x, y, w, h = BOX_2B
    args, fc, vl = [], "", []
    for i, (f, a, b, rev) in enumerate(parts):
        args += ["-i", src(f)]
        fc += (f"[{i}:v]trim=start_frame={a}:end_frame={b + 1},setpts=PTS-STARTPTS,"
               f"crop={w}:{h}:{x}:{y},scale=720:1280,setsar=1{',reverse' if rev else ''},fps=24[v{i}];")
        vl.append(f"[v{i}]")
    nframes = sum(b - a + 1 for _, a, b, _ in parts)
    dur = nframes / 24
    fc += "".join(vl) + f"concat=n={len(parts)}:v=1:a=0,format=yuv420p[v];"

    n = len(parts)
    args += ["-stream_loop", "-1", "-i", os.path.join(VID, ROOM)]
    fc += f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{dur:.3f},asetpts=PTS-STARTPTS[bed];"
    al = ["[bed]"]
    for k, (f, t0, t1, at, muff) in enumerate(lines):
        j = n + 1 + k
        args += ["-i", src(f)]
        d = t1 - t0
        extra = ",lowpass=f=2200,volume=0.8" if muff else ""
        fc += (f"[{j}:a]aresample=48000,aformat=channel_layouts=stereo,atrim={t0}:{t1},asetpts=PTS-STARTPTS,"
               f"afade=t=in:d=0.03,afade=t=out:st={d - 0.03:.3f}:d=0.03{extra},"
               f"adelay={int(at * 1000)}|{int(at * 1000)}[l{k}];")
        al.append(f"[l{k}]")
    fc += "".join(al) + f"amix=inputs={len(al)}:duration=first:normalize=0,apad=whole_dur={dur:.3f},atrim=0:{dur:.3f}[a]"
    out = os.path.join(VID, name + ".mp4")
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *args, "-filter_complex", fc,
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
                    "-c:a", "aac", "-b:a", "192k", out], check=True)
    print(f"{name}: {nframes} frames ({dur:.2f} s)")


if __name__ == "__main__":
    for name, (parts, lines) in CLIPS.items():
        missing = [f for f, *_ in parts if not os.path.exists(src(f))]
        if missing:
            print(f"{name}: skipped, missing {missing}")
            continue
        build(name, parts, lines)
