
> # Projet informatique 2023
  
---

## Description

Ce projet est le code d'une intelligence artificielle capable de jouer au jeu du labyrinthe.

Réalisé par :

#### Soraya Jelti - 21255


---

## Le Code

#### Données Joueur
Les données du joueur se trouve dans la classe Inscription. 

Il peut rentrer l'adresse de son server dans self.servAdd et dans self.inscription son port, son nom et son matricule.

    class Inscription :
        def __init__(self):
            self.servAdd = ('localhost',3000)
            self.inscription = {"request": "subscribe", "port": 8888, "name": "sosoj", "matricules": ["221255"]}
            self.port = 8888



#### Fonctionnement

---
