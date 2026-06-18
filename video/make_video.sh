#!/usr/bin/env bash
# video/make_video.sh
# Usage: place your screen recordings (screen_intro.mp4, screen_perceptron.mp4, ...) in video/ or root,
# or a pre-concatenated screen.mp4. Place webcam.mp4 if you want webcam overlay segments.
# Edit video/webcam_ranges.txt to list start end times (seconds) one per line for overlay.

set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)/.."
VIDEO_DIR="$ROOT_DIR/video"
SCREEN="$ROOT_DIR/screen.mp4"
WEBCAM="$ROOT_DIR/webcam.mp4"
AUDIO="$VIDEO_DIR/rn_basics_audio_fr.mp3"
SRT="$VIDEO_DIR/mini_guide_fr.srt"
OUT="$ROOT_DIR/rn_basics_video_01.mp4"
RANGES_FILE="$VIDEO_DIR/webcam_ranges.txt"

# helper: check files
if [ ! -f "$SCREEN" ]; then
  echo "screen.mp4 not found in repo root. If you recorded segments, please concat them into screen.mp4 or name your main file screen.mp4"
  echo "If you have multiple segments, place them in a file list.txt (format: file 'segment1.mp4'\nfile 'segment2.mp4') and run: ffmpeg -f concat -safe 0 -i list.txt -c copy screen.mp4"
  exit 1
fi

# generate audio if absent
if [ ! -f "$AUDIO" ]; then
  echo "Audio not found. Generating TTS audio using audio/generate_tts.py (requires gTTS and pydub optionally)..."
  python3 audio/generate_tts.py --source "$VIDEO_DIR/mini_guide_video_script_annotated.md" --out "$AUDIO"
fi

# build enable expression from webcam_ranges.txt
ENABLE_EXPR=""
if [ -f "$RANGES_FILE" ] && [ -s "$RANGES_FILE" ]; then
  while read -r start end; do
    # skip empty or comment lines
    if [[ -z "$start" ]] || [[ "$start" == \#* ]]; then
      continue
    fi
    if [ -z "$end" ]; then
      echo "Invalid line in $RANGES_FILE: $start $end"
      continue
    fi
    if [ -z "$ENABLE_EXPR" ]; then
      ENABLE_EXPR="between(t,$start,$end)"
    else
      ENABLE_EXPR="$ENABLE_EXPR+between(t,$start,$end)"
    fi
  done < "$RANGES_FILE"
fi

# assemble
if [ -f "$WEBCAM" ] && [ -n "$ENABLE_EXPR" ]; then
  echo "Assembling with webcam overlay using ranges:"
  cat "$RANGES_FILE"
  # overlay top-right with 10px margin
  ffmpeg -y -i "$SCREEN" -i "$WEBCAM" -i "$AUDIO" \
    -filter_complex "[0:v][1:v] overlay=main_w-overlay_w-10:10:enable='$ENABLE_EXPR' [v]" \
    -map "[v]" -map 2:a \
    -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k \
    -vf "subtitles=$SRT:force_style='FontName=DejaVuSans,FontSize=24'" \
    "$OUT"

elif [ -f "$WEBCAM" ] && [ -z "$ENABLE_EXPR" ]; then
  echo "Webcam file present but no ranges specified (video/webcam_ranges.txt empty). Will overlay webcam for the whole video."
  ffmpeg -y -i "$SCREEN" -i "$WEBCAM" -i "$AUDIO" \
    -filter_complex "[0:v][1:v] overlay=main_w-overlay_w-10:10 [v]" \
    -map "[v]" -map 2:a \
    -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k \
    -vf "subtitles=$SRT:force_style='FontName=DejaVuSans,FontSize=24'" \
    "$OUT"

else
  echo "Assembling without webcam..."
  ffmpeg -y -i "$SCREEN" -i "$AUDIO" \
    -map 0:v -map 1:a \
    -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 192k \
    -vf "subtitles=$SRT:force_style='FontName=DejaVuSans,FontSize=24'" \
    "$OUT"
fi

echo "Output: $OUT"
