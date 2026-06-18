# README_upload.md

Ce fichier contient un court résumé et un lien (à compléter) vers la vidéo finale.

## Vidéo : Mini guide — Comprendre les RN

Vidéo finale (1080p) : [Insérer le lien YouTube/Drive ici]

Sous‑titres (français) inclus : `video/mini_guide_fr.srt`
Notebooks utilisés : `notebooks/01_mlp_numpy.ipynb`, `notebooks/02_mlp_pytorch_enhanced.ipynb`

Pour reproduire la vidéo localement :
1) Installer dépendances : `pip install -r requirements.txt && pip install gTTS pydub`
2) Générer l'audio : `python3 audio/generate_tts.py --source video/mini_guide_video_script_annotated.md --out video/rn_basics_audio_fr.mp3`
3) Placer `screen.mp4` (et `webcam.mp4` si utilisé) à la racine du repo.
4) Assembler la vidéo : `chmod +x video/make_video.sh && ./video/make_video.sh`

(Attention : le fichier MP4 peut être volumineux — consulte `video/upload_guide.md` pour les options d'hébergement et Git LFS si nécessaire.)
