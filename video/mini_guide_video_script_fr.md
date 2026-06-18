# Script vidéo — Mini guide : "Comprendre les RN pas à pas" (français)

Durée cible : 8–12 minutes. But : pour un apprentissage approfondi, tu peux diviser en plusieurs petites vidéos de 4–6 minutes chacune.

Structure et timing recommandé
- 00:00–00:30 — Intro rapide (objectif de la vidéo)
- 00:30–02:30 — Perceptron : intuition + démonstration interactive (notebook NumPy)
- 02:30–04:30 — Régression logistique : fonction sigmoïde, loss, entraînement (visualiser loss)
- 04:30–07:30 — MLP from-scratch : forward, backward, montrer gradient checking
- 07:30–09:30 — Passage à PyTorch : autograd et training loop (exécution rapide)
- 09:30–10:30 — Conseils pour l'apprentissage, prochaines étapes et ressources

Narration détaillée et actions à l'écran (texte à lire / montrer)

00:00 – 00:30 — Intro
- Narration : "Bonjour — je suis [Ton nom]. Dans cette mini-vidéo nous allons comprendre les réseaux de neurones pas à pas : du perceptron à un MLP simple, puis la même chose en PyTorch. L'objectif : que tu puisses démarrer à coder et comprendre pourquoi la rétropropagation fonctionne." 
- Afficher : titre du repo, chemin du notebook notebooks/01_mlp_numpy.ipynb

00:30 – 02:30 — Perceptron (intuition + demo)
- Narration : "Commençons par le perceptron, le plus simple des neurones artificiels. Mathématiquement : z = w·x + b ; sortie = 1 si z>=0 sinon 0. C'est un classifieur linéaire." 
- À l'écran : ouvrir la cellule Perceptron du notebook NumPy, afficher la classe Perceptron.
- Action : Exécuter la cellule qui entraîne sur make_moons et afficher la frontière de décision.
- Narration pendant l'exécution : expliquer les paramètres lr et n_iter, et montrer comment changer le bruit pour voir l'effet.

02:30 – 04:30 — Régression logistique
- Narration : "La régression logistique prend l'idée d'un modèle linéaire mais utilise la sigmoïde et la cross-entropy comme loss, ce qui permet un entraînement via gradient descent." 
- À l'écran : cellule sigmoid + logistic_loss_and_grad. Expliquer brièvement la formule de la loss (log-loss) et le calcul du gradient (probs - y). 
- Action : lancer l'entraînement vectorisé (train_logistic). Montrer la courbe de loss qui décroît.
- Astuce parlée : "Si la loss n'est pas décroissante, vérifie le learning rate et la normalisation des données."

04:30 – 07:30 — MLP from-scratch + gradient checking
- Narration : "Maintenant, un réseau de neurones à une couche cachée. Nous implémentons forward (z1, a1, logits) puis backward en appliquant la règle de la chaîne." 
- À l'écran : afficher la classe SimpleMLP (forward, backward). Expliquer chaque ligne clef : calcul des logits, softmax, cross-entropy, propagation du gradient vers la couche précédente. 
- Action : exécuter une courte boucle d'entraînement sur un petit dataset (digits restreint) et afficher la perte par epoch.
- Gradient checking : expliquer pourquoi c'est utile (détecter bugs). Montrer la cellule numerical_grad et exécuter sur un petit sous-ensemble.
- Narration : "Ici, nous comparons le gradient numérique et analytique — la différence relative doit être très petite (<1e-6 idéalement)."

07:30 – 09:30 — Passage à PyTorch
- Narration : "PyTorch automatise la rétropropagation via autograd. On écrit un Module, et on laisse le framework calculer les gradients." 
- À l'écran : ouvrir notebooks/02_mlp_pytorch.ipynb, afficher la définition de TorchMLP et expliquer brièvement fc1, ReLU, fc2. 
- Action : lancer le training loop (quelques epochs) et montrer que la loss décroît. Si GPU disponible, montrer comment changer device et exécuter rapidement.
- Montrer aussi la version étendue notebooks/02_mlp_pytorch_enhanced.ipynb où l'on suit la norme des gradients et l'histogramme d'activations.

09:30 – 10:30 — Conseils et prochaines étapes
- Narration : "Pour progresser : (1) répète l'implémentation NumPy jusqu'à ce que tu comprennes chaque dérivée ; (2) reproduis-la en PyTorch ; (3) ensuite passe aux notions de stabilisation (initialisation, batchnorm, Adam) ; (4) enfin, abordes les GANs."
- Afficher : plan d'étude (Semaine 1–4) et liens utiles (fast.ai, CS231n, Goodfellow). 
- Fin : "Si tu veux, je peux préparer la version vidéo finale (fichier mp4) ou t'aider à enregistrer pas à pas — dis-moi si tu préfères que j'enregistre l'écran et produise le fichier vidéo pour toi."

Conseils techniques d'enregistrement (OBS / Colab / smartphone)

1) Logiciels : OBS Studio (gratuit) ou enregistrer via Colab + Loom/Chrome extension pour une capture rapide.
2) Résolution : 1280x720 (HD) est suffisante. Framerate 25–30fps.
3) Microphone : un petit micro USB (ou casque) ; teste le bruit de fond et active un filtre passe-bas si disponible.
4) Paramètres OBS recommandés :
   - Encoder : x264 (or NVENC si GPU NVIDIA disponible)
   - Bitrate : 2500–5000 kbps pour 720p
   - Audio bitrate : 128 kbps
5) Préparation :
   - Nettoie ton bureau, augmente la taille de police du notebook (pour la lisibilité), active le mode 'light' si nécessaire.
   - Pré-répète la narration pour rester fluide. Enregistre en segments courts (1–3 min) pour faciliter le montage.
6) Montage simple : iMovie (mac), Shotcut (gratuit), ou OpenShot. Ajoute titres et sous-titres.

Checklist avant d'enregistrer
- [ ] Avoir les notebooks ouverts et exécutés (cellules prêtes à run)
- [ ] Tout le code chargé et les dépendances installées
- [ ] Micro testé et niveau d'entrée audio réglé
- [ ] Caméra désactivée si tu veux uniquement l'écran
- [ ] Poster-script : garder le script à l'écran pour lire la narration ou l'avoir imprimé

Sous-titres et accessibilité
- Fournis le script (inclus ici) comme fichier .srt si tu fais le montage. Pour générer .srt, découpe le script en segments avec timestamps.

Option : je peux produire le fichier vidéo moi‑même
- Je peux te préparer un enregistrement écran mp4 basé sur ce script (narration synthétique ou texte à l'écran). Dis‑moi si tu préfères :
  - Enregistrement brut (écran + son synthétique TTS) — rapide ; ou
  - Écran seul sans narration (tu enregistres ta voix) — je fournis instructions et segments ; ou
  - Je fournis seulement le script et les slides et tu enregistres localement.

---

Fin du guide. Si tu veux, je pousse aussi une version SRT (fichier de sous-titres) et un fichier markdown 'slides' pour servir de base à un export reveal.js. Dis‑moi quelle option tu veux : (A) je fournis seulement les scripts + instructions (déjà fait), (B) j'ajoute .srt et slides.md, (C) je produis un enregistrement mp4 (TTS narration) et le pousse dans le repo.