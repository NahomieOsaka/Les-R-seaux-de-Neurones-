# Guide d'upload pour la vidéo rn_basics_video_01 (YouTube / Google Drive / GitHub)

Ce document explique simplement comment partager la vidéo finale (rn_basics_video_01.mp4) : options, paramètres recommandés et modèle de README à ajouter au dépôt.

Choix d'hébergement (conseils)
- YouTube (recommandé pour diffusion publique et sous-titres) : simple, supporte sous-titres, miniatures, description détaillée et analytics. Pour une vidéo pédagogique c'est habituellement la meilleure option.
- Google Drive / OneDrive (recommandé pour partage privé) : facile à partager via lien (permission view). Utilisé si la vidéo contient des données sensibles ou si tu dois fournir un lien à des encadrants.
- GitHub (non recommandé pour les vidéos volumineuses) : GitHub a des limites de taille et n'est pas optimisé pour stocker binaires lourds. Si vraiment nécessaire, utiliser Git LFS.

Paramètres recommandés pour YouTube
- Visibilité : "Unlisted" si tu veux partager uniquement avec ton équipe; "Public" si tu veux le rendre accessible à tous.
- Titre : "Mini guide : Comprendre les RN — Perceptron → MLP → PyTorch (NahomieOsaka)"
- Description : inclure le lien vers le repo + timestamp sections + dépendances et commandes d'exécution.
- Tags : "réseaux de neurones", "ML", "PyTorch", "NumPy", "tutoriel", "apprentissage profond", "GAN".
- Miniature (thumbnail) : 1280x720 JPG/PNG, lisible, contraste élevé, titre court.
- Langue et sous-titres : définir la langue sur Français. Importer le fichier SRT (video/mini_guide_fr.srt) dans YouTube Studio → Subtitles.
- Paramètres avancés : activer "allow embedding" si tu veux intégrer la vidéo dans le README ou site.

Encodage & qualité
- Conteneur : MP4 (H.264), audio AAC 128–192 kbps. Framerate 30fps.
- Résolution recommandée : 1920x1080 (1080p) si tu as enregistré en 1080p; sinon 1280x720 acceptable.
- CRF/bitrate : CRF 18 (ffmpeg) ou video bitrate 8–12 Mbps pour 1080p en H.264.

Importer sous‑titres sur YouTube
1. Ouvre YouTube Studio → Subtitles. 
2. Sélectionne la vidéo → ADD LANGUAGE → Français → Upload file → Choose file → sélectionne video/mini_guide_fr.srt. 
3. Vérifie le timing dans l'éditeur et publie.

Modèle de description (copier-coller dans YouTube)
"""
Mini guide : Comprendre les RN — Perceptron → MLP → PyTorch
Auteur : NahomieOsaka
Repo & notebooks : https://github.com/NahomieOsaka/Les-R-seaux-de-Neurones-/tree/rn-basics

Chapitres:
00:00 Intro
00:30 Perceptron (demo)
02:30 Régression logistique
04:30 MLP from-scratch + gradient checking
07:30 PyTorch (autograd et training loop)
09:30 Conseils & prochaines étapes

Sous-titres : fournis (français)
Dépendances (pour reproduire) : voir requirements.txt dans le repo

Contact : NahomieOsaka (via GitHub)
"""

Partager via Google Drive (privé)
1. Uploader rn_basics_video_01.mp4 dans Google Drive.
2. Clic droit → Get link → choisir 'Anyone with the link' : Viewer (si tu veux le rendre consultable sans compte) ou Restreint si tu veux contrôler l'accès.
3. Copier le lien et le coller dans le README du repo ou partager dans Slack / email.

Pousser la vidéo sur GitHub (avec Git LFS) — uniquement si tu veux stocker dans le repo
1. Installer Git LFS (https://git-lfs.github.com/) et initialiser :
   git lfs install
2. Configurer les types à tracker (par ex. mp4) :
   git lfs track "*.mp4"
   git add .gitattributes
3. Ajouter le fichier et committer comme d'habitude :
   git add rn_basics_video_01.mp4
   git commit -m "Ajout video rn_basics 1080p"
   git push origin rn-basics
Note : Git LFS stocke le contenu ailleurs, mais cela peut consommer quota selon ton plan GitHub.

Automatisation d'upload Drive (optionnel)
- rclone est un outil robuste pour uploader en ligne de commande vers Drive, OneDrive, S3, etc. Exemple (après config rclone):
  rclone copy rn_basics_video_01.mp4 remote:folder -P

README à ajouter au dépôt (snippet)
```markdown
## Vidéo — Mini guide RN (Perceptron → MLP → PyTorch)

La vidéo pédagogique est disponible ici : [lien à insérer]

Sous‑titres (FR) : `video/mini_guide_fr.srt`
Notebooks utilisés dans la démo : `notebooks/01_mlp_numpy.ipynb`, `notebooks/02_mlp_pytorch_enhanced.ipynb`

Pour reproduire localement :
1. Installer dépendances : `pip install -r requirements.txt` + `pip install gTTS pydub`
2. Générer l'audio TTS (optionnel) : `python3 audio/generate_tts.py`
3. Assembler la vidéo : `./video/make_video.sh` (voir `video/README.md` pour détails)
```

Checklist finale avant upload
- [ ] Vérifier audio (volume homogène, sans clipping)
- [ ] Vérifier sous‑titres (timing & fautes)
- [ ] Créer une miniature 1280x720
- [ ] Remplir la description YouTube (avec timestamps)
- [ ] Tester le lien partagé (incognito si 'Unlisted')

Si tu veux, je peux :
- générer automatiquement le README de dépôt (avec le lien que tu me donnes après upload) et le committer sur rn-basics ;
- fournir la commande rclone prête à l'emploi (si tu veux uploader vers Google Drive depuis terminal) ;
- ou te guider pas à pas pour l'upload (je peux rester ici et t'aider pendant l'upload).
