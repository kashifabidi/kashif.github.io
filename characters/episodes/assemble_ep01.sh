#!/usr/bin/env bash
# Rebuild the EP01 assembly from approved finals, in script order.
set -e
cd "$(dirname "$0")/../shots/video"
FF=${FFMPEG:-$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")}
CLIPS=(EP01_SH01_final EP01_SH02a_final EP01_SH02b_final EP01_SH02c_final EP01_SH03a_final EP01_SH03b_final EP01_SH03c_final EP01_SH04a_final EP01_SH04b_final EP01_SH04c_final EP01_SH05a_final EP01_SH05b_final EP01_SH06a_final EP01_SH07a_final EP01_SH07b_final EP01_SH07c_final)
ARGS=(); F=""; N=0
for c in "${CLIPS[@]}"; do
  ARGS+=(-i "$c.mp4")
  F+="[$N:v]fps=24,scale=720:1280,format=yuv420p,setsar=1[v$N];[$N:a]aresample=48000,aformat=channel_layouts=stereo[a$N];"
  N=$((N+1))
done
for i in $(seq 0 $((N-1))); do F+="[v$i][a$i]"; done
F+="concat=n=$N:v=1:a=1[v][a]"
"$FF" -hide_banner -loglevel error -y "${ARGS[@]}" -filter_complex "$F" -map "[v]" -map "[a]" -c:v libx264 -crf 16 -preset slow -c:a aac -b:a 192k EP01_assembly.mp4
echo "EP01_assembly.mp4 built from ${#CLIPS[@]} clips"
