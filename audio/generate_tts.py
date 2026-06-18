from gtts import gTTS
from pathlib import Path
import textwrap

# audio/generate_tts.py
# Usage: python audio/generate_tts.py [--source video/mini_guide_video_script_annotated.md] [--out video/rn_basics_audio_fr.mp3]

import argparse

def chunk_text(text, max_chars=4000):
    """gTTS can have limits on very long texts; split into sensible chunks on sentence boundaries."""
    sentences = text.replace('\n', ' ').split('. ')
    chunks = []
    current = ''
    for s in sentences:
        if len(current) + len(s) + 2 > max_chars:
            chunks.append(current.strip())
            current = s + '. '
        else:
            current += s + '. '
    if current.strip():
        chunks.append(current.strip())
    return chunks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='video/mini_guide_video_script_annotated.md')
    parser.add_argument('--out', type=str, default='video/rn_basics_audio_fr.mp3')
    args = parser.parse_args()

    src = Path(args.source)
    if not src.exists():
        print(f"Source script not found: {src}. Please check the path.")
        return
    text = src.read_text(encoding='utf-8')

    # Option: preprocess text to improve TTS prosody for sarcasm: add pauses and parentheses
    # The annotated script already contains cues (pauses, ellipses, parenthesis)

    print('Splitting text into chunks for TTS...')
    chunks = chunk_text(text)
    print(f'Generating {len(chunks)} TTS chunk(s)')

    # generate each chunk and append
    temp_files = []
    for i, ch in enumerate(chunks):
        chunk_file = Path(f"video/tts_chunk_{i}.mp3")
        print(f'  generating chunk {i} -> {chunk_file}')
        tts = gTTS(text=ch, lang='fr', slow=False)
        tts.save(str(chunk_file))
        temp_files.append(chunk_file)

    # concatenate chunks into single mp3
    # naive concatenation by binary append is not reliable for mp3 headers; use pydub if available
    try:
        from pydub import AudioSegment
        combined = AudioSegment.empty()
        for f in temp_files:
            combined += AudioSegment.from_mp3(str(f))
        combined.export(str(args.out), format='mp3')
        print('Combined audio saved to', args.out)
    except Exception as e:
        # fallback: simple binary append (may not always work); still attempt
        print('pydub not available or failed, falling back to binary append (less reliable). Error:', e)
        with open(args.out, 'wb') as wfd:
            for f in temp_files:
                with open(f, 'rb') as fd:
                    wfd.write(fd.read())
        print('Saved (binary-append) to', args.out)

    print('Cleaning temporary chunk files...')
    for f in temp_files:
        try:
            f.unlink()
        except Exception:
            pass
    print('Done.')

if __name__ == '__main__':
    main()
