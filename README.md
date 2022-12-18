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
## Lancement du programme

## Déroulement du programme

## Contrôle qualité

flake8 --format=html --htmldir=flake-report ProjectTournoi
