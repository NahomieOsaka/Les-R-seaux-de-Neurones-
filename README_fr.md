# Ajouts pour rn-basics

J'ai ajouté plusieurs ressources pédagogiques et outils pour t'aider à apprendre pas à pas et pour vérifier ton environnement.

Fichiers ajoutés :
- notebooks/01_mlp_numpy_exercices.ipynb : exercices guidés et solutions pour renforcer les notions du notebook NumPy.
- notebooks/02_mlp_pytorch_enhanced.ipynb : version étendue du notebook PyTorch avec visualisations des normes de gradient, histogrammes d'activations, et exercices.
- tests/auto_test_env_and_training.py : script léger pour vérifier l'environnement (packages) et lancer un court entraînement d'un MLP PyTorch pour vérifier que tout tourne (CPU/GPU) et que la loss diminue.
- README_fr.md : mis à jour pour décrire les nouveaux fichiers et comment les utiliser.

Utilisation rapide du script de test :
- python tests/auto_test_env_and_training.py

Il fera :
- vérifier les dépendances listées dans requirements.txt (présence importable),
- exécuter un entraînement court (5 epochs) sur un petit sous-ensemble des digits et vérifier que la loss diminue (contrôle basique).