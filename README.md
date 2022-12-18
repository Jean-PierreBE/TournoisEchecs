# Projet 4 OpenClassRoom : logiciel de gestion de tournoi d'Echecs
## Présentation du projet
Le but de ce projet est de créer un logiciel de gestion de tournois d'échecs qui fonctionne hors ligne.
8 joueurs participent à un tournoi qui se compose de 4 rounds et chaque round comprend 4 matchs avec 2 joueurs chacun.
Avec le logiciel développé , les organisateurs vont pouvoir créer les joueurs (8 au minimum) , encoder les tournois et
sortir des rapports sur le déroulement des tournois.
Chaque tournoi pourra être arrêté temporairement à tout moment durant son déroulement pour diverses raisons : heure tardive, 
joueur malade , élément imprévu.
Le score de chaque match pourra être modifié durant chaque round.

## composition
Tous les fichiers .py necessaires au fonctionnement du logiciel se trouvent dans le répertoire ProjectTournoi.
Les autres fichiers sont :
- README.md qui contient des informations sur le logiciel
- requirements.txt contient les packages necessaires au bon fonctionnement du logiciel
- tox.ini permet de paramétrer flake8 pour voir si le programme répond aux normes pep8

## Installation
- choisissez votre répertoire où exécuter vos programmes python
- créer votre environnement virtuel
- installer les packages python du fichier requirements.txt en lançant la commande suivante 
  - `pip install -r requirements.txt`

les packages installés sont les suivants :
- tinydb : gestion de la base de données tinydb
- prettytable : gestion de tableau pour les différents affichages
- jsons : permet de sérializer les objets pour les intégrer dans tinydb

## Lancement du programme
On lance le programme en tapant sur la ligne de commande :
- `python -m ProjectTournoi`

## Déroulement du programme

## Contrôle qualité
Pour vérifier la qualité du code , on peut lancer la commande suivante :
- `flake8 --format=html --htmldir=flake-report ProjectTournoi`
Le rapport sortira en format html dans le répertoire flake-report

pour cela il faut installer :
- flake8 : contrôle du code pour vérifier la compatibilité avec les normes pep8
- flake8-html : permet de sortir le rapport flake8 sous format html
- flake8-functions : permet d'ajouter des contrôles au niveau des fonctions (ex : longueur maximale des fonctions)

le fichier tox.ini contient la configuration pour flake8.
- `max-line-length = 119` : la longueur maximale de chaque ligne ne peut pas dépasser 119 caractères
- `max-function-length = 50` : la longueur maximale de chaque fonction ne peut pas dépasser 50 lignes
- `ignore = CFQ002, CFQ004` : évite les erreurs 
                                - CFQ002 : nombre d'arguments en entrée trop élevés (> 6)
                                - CFQ004 : nombre d'éléments en retour trop élevés (> 3)

Ces paramètres peuvent être modifiés



