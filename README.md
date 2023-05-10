
> # Projet informatique 2023
  
---

## Description

Ce projet est le code d'une intelligence artificielle capable de jouer au jeu du labyrinthe.

Réalisé par :

#### Soraya Jelti - 21255


---

## Le Code

### Données Joueur
Les données du joueur se trouve dans la classe Inscription. 

Il peut rentrer l'adresse de son server dans self.servAdd et dans self.inscription son port, son nom et son matricule.

    class Inscription :
        def __init__(self):
            self.servAdd = ('localhost',3000)
            self.inscription = {"request": "subscribe", "port": 8888, "name": "sosoj", "matricules": ["221255"]}
            self.port = 8888



### Fonctionnement
La classe Inscription contient la partie réseau et la classe Game contient le code du jeux.

Premièrement, l'IA va se connecter au gestionnaire de partie ([disponible ici](https://github.com/qlurkin/PI2CChampionshipRunner)) et envoyer un pong à la requête ping. Elle sera alors correctement inscrite et attendra qu'un match se lance. 

Elle va ensuite recevoir une requête move à la laquelle elle va répondre en renvoyant la tuile à placer dans le jeu, l'entrée qu'elle veut utiliser et la nouvelle position qu'elle veut atteindre.

### Bibliothèque utilisées
Pour ce code, les bibliothèques suivantes ont été utilisées :

  - json
  - random
  - socket
  

---
