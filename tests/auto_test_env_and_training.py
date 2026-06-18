#!/usr/bin/env python3
"""
tests/auto_test_env_and_training.py

Script léger pour vérifier l'environnement et lancer un court entraînement PyTorch.
Vérifie que les packages sont importables et qu'un MLP s'entraîne (loss décroissante).
"""

import sys
import importlib
import time

REQUIRED = ['numpy', 'torch', 'matplotlib', 'sklearn']

missing = []
for pkg in REQUIRED:
    try:
        importlib.import_module(pkg)
    except Exception:
        missing.append(pkg)

if missing:
    print('Packages manquants :', missing)
    print('Installe via: pip install -r requirements.txt')
    sys.exit(2)

print('Packages essentiels présents. Test de training rapide...')

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np

# Préparer un dataset très petit
digits = load_digits()
X = digits.data / 16.0
y = digits.target
mask = y < 3
X = X[mask]
y = y[mask]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train_t = torch.tensor(X_train, dtype=torch.float32)
y_train_t = torch.tensor(y_train, dtype=torch.long)
train_ds = TensorDataset(X_train_t, y_train_t)
train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)

class TorchMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


def run_short_training(device='cpu'):
    model = TorchMLP(input_dim=X_train.shape[1], hidden_dim=32, output_dim=3).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.05)
    losses = []
    for epoch in range(5):
        running_loss = 0.0
        for xb, yb in train_loader:
            xb = xb.to(device)
            yb = yb.to(device)
            optimizer.zero_grad()
            logits = model(xb)
            loss = criterion(logits, yb)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * xb.size(0)
        epoch_loss = running_loss / len(train_loader.dataset)
        losses.append(epoch_loss)
        print(f'Epoch {epoch}, loss={epoch_loss:.4f}')
    return losses

# test CPU
losses_cpu = run_short_training(device='cpu')

# test GPU if available
if torch.cuda.is_available():
    print('GPU disponible, test rapide sur GPU...')
    losses_gpu = run_short_training(device='cuda')
else:
    print('GPU non disponible — test CPU uniquement')

# vérifier décroissance moyenne
if losses_cpu[-1] < losses_cpu[0]:
    print('\nTest réussi : loss diminue sur CPU (basique).')
else:
    print('\nAttention : la loss n\'a pas diminué sur CPU — cela peut indiquer un problème logiciel ou un hyperparamètre à ajuster.')

print('Script de test terminé.')
