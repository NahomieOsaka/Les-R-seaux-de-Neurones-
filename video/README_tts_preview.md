# Note pour l'utilisateur

Le fichier `video/tts_preview.md` contient un court extrait (30-40s) du script. Pour générer et écouter un aperçu TTS :

1) Assure-toi d'activer ton environnement virtuel et d'avoir installé gTTS et pydub :
   pip install gTTS pydub

2) Génère le MP3 d'aperçu :
   python3 audio/generate_tts.py --source video/tts_preview.md --out video/tts_preview.mp3

3) Écoute le fichier (exemples) :
   ffplay video/tts_preview.mp3
   # ou sur macOS
   open video/tts_preview.mp3

Si le ton te convient, exécute la commande complète pour générer `video/rn_basics_audio_fr.mp3` à partir du script annoté.
