# Script de Chiffrement CSS

Ce script Python implémente des fonctions pour simuler les LFSRs de 17 et 25 bits, générer des séquences de chiffrement CSS, et exécuter une attaque pour déterminer les états initiaux des LFSRs à partir de sorties partiellement connues.
## Auteur
-Ali Hargas 22104524
-Soufiane El Moussafer
## Fonctionnalités

### Simulation de LFSRs

- `LFSR17(coef, entree, rep)`: Simule un LFSR de 17 bits.
- `LFSR25(coef, entree, rep)`: Simule un LFSR de 25 bits.

### Génération de séquences de chiffrement CSS

- `css(rep)`: Produit une séquence de chiffrement basée sur les sorties des LFSRs de 17 et 25 bits.

### Attaque cryptanalytique

- `attaque(gene)`: Exécute une attaque pour retrouver les états initiaux des LFSRs en utilisant les sorties observées.

### Utilitaires

- `liste_en_bits(lst)`: Convertit une liste de nombres en une chaîne de bits.
- `addition_binaire(seq1, seq2)`: Réalise une addition binaire de deux séquences de bits.
- `addition_binaire3(seq1, seq2, c)`: Additionne deux séquences binaires avec une retenue.

### Tests

- `Generateur()`: Génère des sorties cryptées utilisées pour tester l'efficacité de l'attaque.
- `test_LFSR17()`, `test_LFSR25()`: Fonctions pour tester les LFSRs.

## Utilisation de la bibliothèque `random`

Le script utilise la bibliothèque `random` de Python pour plusieurs fonctionnalités clés :

### Génération d'états initiaux aléatoires
- Simulation des LFSRs : Les fonctions `LFSR17` et `LFSR25` nécessitent un état initial pour commencer la simulation. L'état initial de ces registres est généré de manière aléatoire en utilisant `random.randint(0, 1)` pour remplir les listes qui représentent l'état du registre à décalage. 
Cela permet de simuler un démarrage réaliste et aléatoire des LFSRs comme il se produirait dans une implémentation réelle.

### Tests et validation
- Fonctions de test (`test_LFSR17`, `test_LFSR25`) : Pour vérifier que les LFSRs fonctionnent correctement, ces fonctions génèrent des séquences de tests en initialisant les LFSRs avec des valeurs aléatoires. 
Cela aide à s'assurer que les LFSRs fonctionnent correctement sous différentes conditions initiales.

## Installation

Python 3 est installé sur la machine éxecutant le code. 
Aucune bibliothèque externe n'est nécessaire.

## Utilisation

Le script est éxecutable avec la ligne de commande :

```bash
python Attaque_contre_le chiffrement_à_flot_CSS.py
