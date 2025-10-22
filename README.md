# 🗂️ Application de Gestion de Tâches (Python + PySide6)

## 📋 Description

Cette application de bureau permet de gérer des tâches et leurs commentaires associés, à la manière d’un mini-Trello.

Elle repose sur une architecture **MVC (Modèle - Vue - Contrôleur)**, utilise **PySide6** pour l’interface graphique, et une **persistance locale** via **SQLite**.

Les principales fonctionnalités incluent :

- Création, lecture, modification et suppression de tâches (CRUD complet)
- Ajout de commentaires liés à chaque tâche
- Clôture / réouverture d’une tâche
- Validation des données (intégrité, cohérence des états)
- Sauvegarde automatique des données

---

## ⚙️ Installation

### 1️⃣ Prérequis

- **Python 3.13.1**
- **pip** installé
- Environnement virtuel recommandé

### 2️⃣ Installation des dépendances

```bash
git clone du repo
cd task-manager-pyside6
python -m venv venv
source venv/bin/activate  # sous Linux/Mac
venv\\Scripts\\activate     # sous Windows
pip install -r requirements.txt

```

### 3️⃣ Lancement de l’application

```bash
python main.py
```

L’application s’ouvrira dans une fenêtre PySide6 avec la liste des tâches.

## 🧩 Architecture (MVC)

L’application suit strictement le **modèle MVC** :

### **Modèle (Model)**

- Gère la persistance des données (SQLite)
- Contient les classes métier : `Task`, `Comment` etc…
- Fournit les méthodes CRUD et de validation

### **Vue (View)**

- Interface graphique en **PySide6**
- Présente la liste des tâches, le formulaire de création/modification et la zone de commentaires
- Aucune logique métier, uniquement l’affichage et les signaux utilisateurs

### **Contrôleur (Controller)**

- Fait le lien entre la Vue et le Modèle
- Gère les événements utilisateurs, applique la logique métier, met à jour la Vue
- Vérifie la cohérence des états (tâche ouverte / close, etc.)

---

## 💾 Persistance des données

- Les données sont enregistrées localement dans un fichier **SQLite (`tasks.db`)**.
- Cela permet de conserver les informations entre deux sessions, sans serveur distant.
- La couche Modèle encapsule totalement cette logique pour permettre un futur remplacement éventuel (par ex. API REST).

---

## 🧠 Logique métier

Une tâche possède :

- un **titre** (obligatoire)
- une **description**
- un **état** (`À faire` / `en cours` / `clôturée`)
- une **liste de commentaires** (liés par un ID de tâche)

Chaque commentaire contient :

- un **contenu textuel**
- une **date de création**

Le contrôleur vérifie les transitions d’état :

- Impossible d’ajouter un commentaire à une tâche clôturée.
- La réouverture d’une tâche est autorisée.

---

## 🧰 Technologies principales

| Composant           | Librairie / outil    |
| ------------------- | -------------------- |
| Interface graphique | PySide6              |
| Base de données     | SQLite (via sqlite3) |
| Architecture        | MVC                  |
| Langage             | Python 3.13.1        |

## 🧩 Structure du projet

```
task-manager/
│
├── main.py
├── models/
│   ├── task_model.py
│   ├── comment_model.py
│   └── database.py
│
├── views/
│   ├── main_window.py
│   ├── task_list_view.py
│   └── task_form_view.py
│
├── controllers/
│   ├── task_controller.py
│   └── comment_controller.py
│
├── assets/
│   └── icons/
│
├── requirements.txt
└── README.md

```

## 🧩 EXPLICATIONS

Ce projet a été conçu avec une approche **pédagogique et modulaire** :

- **Choix du MVC** : séparer clairement les responsabilités, faciliter la maintenance et les tests unitaires.
- **Choix de PySide6** : framework officiel Qt pour Python, riche, maintenu et performant pour les applications desktop modernes.
- **Choix de SQLite** : léger, embarqué, sans dépendance serveur. Adapté aux applications locales.
- **Validation côté modèle** : éviter les erreurs de saisie et garantir l’intégrité métier.
- **Signal/Slot Qt (gestion des évènements)** : assure une communication fluide entre l’interface et la logique métier. Exemple :

```python
button = QPushButton("Ajouter une tâche")

# Slot (l'équivalent du "listener" en JavaScript)
def handle_click():
    print("Tâche ajoutée !")

# 'clicked' est le signal (l'équivalent du "trigger" en JavaScript)
button.clicked.connect(handle_click)

# Le .connect() fait le lien entre le signal et le slot

```

L’objectif final est d’obtenir une **application propre, extensible et facilement testable**, pouvant évoluer vers une version en réseau ou connectée à une API.