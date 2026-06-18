# Slides outline (markdown)

---
# Comprendre les RN — Mini guide

Objectif : implémenter et comprendre perceptron, logistic regression, MLP from-scratch et PyTorch

---
# 1) Perceptron
- z = w·x + b
- sortie = 1(z>=0)
- Demo : notebook -> make_moons

---
# 2) Régression logistique
- Sigmoïde
- Cross-entropy (log-loss)
- Gradient = probs - y

---
# 3) MLP from-scratch
- Forward: z1 = XW1 + b1, a1 = ReLU(z1), logits = a1 W2 + b2
- Backward: appliquer chain rule
- Gradient checking

---
# 4) PyTorch
- Module, autograd, training loop
- Device (CPU/GPU)

---
# Ressources & prochaines étapes
- notebooks/ dans le repo
- fast.ai, CS231n, Goodfellow
