# Générateur de Groupes Aléatoires

Ce projet est une interface en ligne de commande (CLI) Python qui génère des groupes aléatoires à partir d'une liste de noms dans un fichier texte.

## Prérequis

- Python 3.6 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

Suivez ces étapes pour installer et configurer le projet dans un environnement virtuel :

1. Clonez le dépôt (ou téléchargez le code source) :

```
git clone https://github.com/hashgo44/random_groups
cd random_groups
```

2. Créez un environnement virtuel :

```
python -m venv .env
```

3. Activez l'environnement virtuel :

- Sur Windows :

```
.env\Scripts\activate
```

- Sur macOS et Linux :

```
source .env/bin/activate
```

4. Installez les dépendances :

```
pip install -r requirements.txt
```

## Utilisation

Après avoir activé l'environnement virtuel, vous pouvez utiliser le script comme suit :

```
python main.py -i noms.txt -g 4 -o groupes_generes.txt
```

Où :

- `-i noms.txt` est le fichier d'entrée contenant les noms
- `-g 4` est la taille des groupes (optionnel, par défaut 3)
- `-o groupes_generes.txt` est le fichier de sortie (optionnel, par défaut 'groupes.txt')

## Désactivation de l'environnement virtuel

Lorsque vous avez terminé d'utiliser le projet, vous pouvez désactiver l'environnement virtuel en exécutant :

```
deactivate
```

Cela vous ramènera à votre environnement Python global.
