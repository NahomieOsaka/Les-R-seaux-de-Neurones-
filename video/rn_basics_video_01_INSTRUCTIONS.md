Rendu demandé : rn_basics_video_01.mp4

Note technique : Le rendu MP4 a été demandé et les assets sont prêts (script, storyboard, srt). Dans cet environnement je ne peux pas stocker de véritables assets vidéo binaires au format mp4 via l'API. Pour obtenir le MP4 réel, tu as deux options :

1) Je fournis un script de rendu (FFmpeg + TTS) que tu peux exécuter localement pour générer le MP4 final à partir des assets déjà présents dans video/ (srt + script + slides). Je peux générer ce script immédiatement.

2) Je fournis un lien de téléchargement si tu préfères que je génère le MP4 hors-plateforme et que je le téléverse (nécessite que je puisse créer des assets binaires, ce qui n'est pas possible ici). 

Si tu veux le rendu localement (option 1), exécute ce script depuis la racine du repo :

- Installe gTTS : pip install gTTS
- Génère l'audio TTS depuis script (video/mini_guide_fr.srt ou video/mini_guide_video_script_fr.md)
- Utilise ffmpeg pour assembler l'audio et les captures d'écran (ou vidéos segmentées)

Je peux générer et commiter le script shell qui :
- génère audio TTS via gTTS (voix française)
- crée un fichier video à partir d'une capture écran simulée (placeholder images) ou segments fournis
- assemble audio + images en MP4 1080p H.264

Veux-tu que je commite ce script de rendu (recommandé) ?