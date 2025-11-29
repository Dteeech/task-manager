# Gestionnaire de Tâches - Application Desktop Python

##  Description du projet

Application desktop de gestion de tâches développée en Python avec interface graphique PySide6. Cette application permet de créer, modifier, supprimer et organiser des tâches avec une persistance locale via SQLite.

**Objectifs pédagogiques :**
- Développer une application desktop complète avec interface graphique
- Implémenter un CRUD complet avec persistance locale
- Utiliser PySide6 pour l'interface utilisateur
- Appliquer une architecture MVC claire et structurée
- Gérer les états métiers et la validation des données

---

##  Fonctionnalités principales
### Accessibilité
-  **Darkmode - Lightmode**
### Gestion des tâches (CRUD)
-   **Créer** une nouvelle tâche avec titre et description
-   **Afficher** la liste de toutes les tâches
-   **Modifier** une tâche existante (titre, description, statut)
-   **Supprimer** une tâche avec confirmation
-   **Changer le statut** d'une tâche (À faire / En cours / Terminée)

### Interface utilisateur
-  Interface moderne et intuitive avec widgets personnalisés
-  Vue détaillée pour chaque tâche avec édition WYSIWYG
-  Support d'images de bannière pour les tâches
-  Indicateurs visuels de statut avec code couleur
-  Navigation fluide entre liste et vue détail

### Persistance des données
-  Sauvegarde automatique dans base SQLite locale
-  Synchronisation en temps réel des modifications
-  Horodatage automatique (création et modification)

---

##  Installation et lancement

### Prérequis
- **Python 3.13.1** ou supérieur
- **pip** (gestionnaire de paquets Python)
- **Git** pour cloner le repository

### Cloner le projet

```bash
git clone https://github.com/Dteeech/task-manager.git
cd task-manager
```

### Créer un environnement virtuel

**Linux/macOS :**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Lancer l'application

```bash
python3 main.py
```

---

## Architecture MVC

L'application suit une architecture **Modèle-Vue-Contrôleur (MVC)** stricte pour une séparation claire des responsabilités :

### Modèle (Model)
**Localisation :** `models/`

- **`task_model.py`** : Gestion des opérations CRUD sur les tâches
- **`database.py`** : Connexion et initialisation de la base SQLite

**Responsabilités :**
- Persistance des données (SQLite)
- Logique métier et validation des données
- Opérations CRUD (Create, Read, Update, Delete)
- Gestion de l'intégrité des données

### Vue (View)
**Localisation :** `views/`

- **`main_window.py`** : Fenêtre principale avec liste des tâches
- **`task_detail_view.py`** : Vue détaillée d'une tâche avec édition
- **`widgets/task_row_widget.py`** : Widget personnalisé pour afficher une tâche dans la liste

**Responsabilités :**
- Interface graphique PySide6
- Affichage des données
- Capture des événements utilisateur (via signaux Qt)
- Aucune logique métier

### Contrôleur (Controller)
**Localisation :** `controllers/`

- **`task_controller.py`** : Orchestration entre modèle et vues

**Responsabilités :**
- Liaison entre Vue et Modèle
- Gestion des événements utilisateur
- Application de la logique métier
- Mise à jour de l'interface

---

## Structure du projet

```
task-manager/
│
├── main.py                          # Point d'entrée de l'application
├── requirements.txt                 # Dépendances Python
├── README.md                        # Documentation
│
├── models/                          # Couche Modèle (données)
│   ├── __init__.py
│   ├── database.py                  # Gestion SQLite
│   └── task_model.py                # Modèle Task (CRUD)
│
├── views/                           # Couche Vue (interface)
│   ├── __init__.py
│   ├── main_window.py               # Fenêtre principale
│   ├── task_detail_view.py          # Vue détail tâche
│   └── widgets/                     # Widgets personnalisés
│       ├── __init__.py
│       ├── task_row_widget.py       # Widget ligne de tâche
│       └── task_card_widget.py      # Widget carte de tâche
│
├── controllers/                     # Couche Contrôleur (logique)
│   ├── __init__.py
│   └── task_controller.py           # Contrôleur principal
│
├── assets/                          # Ressources statiques
│   └── icons/                       # Icônes SVG
│       ├── pen.svg
│       └── trash.svg
│
└── data/                            # Base de données (généré)
    └── tasks.db                     # SQLite database
```

---

## Modèle de données

### Table `tasks`

| Colonne      | Type    | Contraintes           | Description                           |
|--------------|---------|-----------------------|---------------------------------------|
| `id`         | INTEGER | PRIMARY KEY AUTOINCREMENT | Identifiant unique                    |
| `title`      | TEXT    | NOT NULL              | Titre de la tâche (obligatoire)       |
| `description`| TEXT    |                       | Description détaillée                 |
| `status`     | TEXT    | DEFAULT 'À faire'     | Statut (À faire / En cours / Terminée)|
| `image_path` | TEXT    |                       | Chemin vers l'image de bannière       |
| `created_at` | TEXT    | DEFAULT CURRENT_TIMESTAMP | Date/heure de création            |
| `updated_at` | TEXT    | DEFAULT CURRENT_TIMESTAMP | Date/heure de dernière modification|

### États possibles d'une tâche

| Statut      | Couleur  | Description                    |
|-------------|----------|--------------------------------|
| À faire     | 🟠 Orange| Tâche créée, pas encore démarrée|
| En cours    | 🔵 Bleu  | Tâche en cours de réalisation  |
| Terminée    | 🟢 Vert  | Tâche complétée                |

---

## Technologies utilisées

| Composant             | Technologie          | Version | Rôle                                  |
|-----------------------|----------------------|---------|---------------------------------------|
| **Langage**           | Python               | 3.13.1  | Langage de programmation              |
| **Interface graphique** | PySide6            | 6.8.1   | Framework Qt pour Python              |
| **Base de données**   | SQLite               | 3.x     | Persistance locale                    |
| **Architecture**      | MVC                  | -       | Séparation des responsabilités        |

---

##  Utilisation de l'application

### 1. Créer une tâche
1. Saisir un **titre** dans le champ prévu
2. (Optionnel) Ajouter une **description**
3. Cliquer sur **"Ajouter"**
4. La tâche apparaît dans la liste avec le statut "À faire"

### 2. Modifier une tâche
1. Cliquer sur l'icône **✏️ (crayon)** sur la ligne de la tâche
2. La vue détaillée s'ouvre avec :
   - Titre de la tâche
   - Bannière image (modifiable)
   - Description éditable (zone de texte enrichie)
   - Sélecteur de statut
3. Modifier les informations souhaitées
4. Cliquer sur **"💾 Enregistrer"**
5. Cliquer sur **"← Retour"** pour revenir à la liste

### 3. Changer le statut
**Méthode 1 - Depuis la liste :**
- Utiliser le menu déroulant de statut directement sur la ligne de la tâche

**Méthode 2 - Depuis la vue détail :**
- Ouvrir la tâche en mode édition
- Sélectionner le nouveau statut dans le menu déroulant
- Le changement est pris en compte automatiquement

### 4. Supprimer une tâche
1. Cliquer sur l'icône **🗑️ (poubelle)** sur la ligne de la tâche
2. Confirmer la suppression dans la boîte de dialogue
3. La tâche est supprimée définitivement

### 5. Ajouter une image de bannière
1. Ouvrir une tâche en mode édition
2. Cliquer sur **"Changer la bannière"**
3. Sélectionner une image (PNG, JPG, JPEG)
4. L'image s'affiche automatiquement

---

## Choix techniques et justifications

### Pourquoi PySide6 ?
- **Framework Qt officiel** pour Python, maintenu par The Qt Company
- **Riche en widgets** et composants UI modernes
- **Signal/Slot** : système élégant de gestion d'événements
- **Cross-platform** : fonctionne sur Windows, macOS, Linux
- **Performance** : rendu natif et réactivité

### Pourquoi SQLite ?
- **Léger et embarqué** : pas de serveur à installer
- **Zero-configuration** : fonctionne "out of the box"
- **Fiable** : largement utilisé et testé
- **Adapté au local** : idéal pour une application desktop
- **Évolutif** : peut être remplacé par PostgreSQL/MySQL si besoin

### Pourquoi MVC ?
- **Séparation des responsabilités** : chaque couche a un rôle distinct
- **Maintenabilité** : modifications isolées sans impact sur les autres couches
- **Testabilité** : possibilité de tester chaque composant indépendamment
- **Réutilisabilité** : modèles et contrôleurs réutilisables
- **Collaboration** : plusieurs développeurs peuvent travailler en parallèle

### Signal/Slot (Qt)
Le mécanisme Signal/Slot de Qt permet une communication événementielle découplée :

```python
# Exemple : bouton connecté à une action
self.add_button.clicked.connect(self.create_task)
# 'clicked' = signal émis par le bouton
# 'create_task' = slot (fonction) qui réagit au signal
```

**Avantages :**
- Découplage entre émetteur et récepteur
- Type-safe avec support PyQt
- Gestion automatique de la durée de vie des objets

---

## Résolution de problèmes

### L'application ne se lance pas
**Solution :**
```bash
# Vérifier la version Python
python3 --version  # Doit être >= 3.13

# Réinstaller les dépendances
pip install --upgrade -r requirements.txt

# Vérifier PySide6
python3 -c "import PySide6; print(PySide6.__version__)"
```

### Erreur "Internal C++ object already deleted"
**Cause :** Widget Qt détruit côté C++ mais référence Python subsiste

**Solution :** Déjà corrigée dans le code via :
- Création des widgets avec `parent` explicite
- Protection `try/except` autour des opérations Qt critiques
- Gestion correcte du `QStackedWidget`

### Base de données corrompue
**Solution :**
```bash
# Supprimer la base et la recréer
rm data/tasks.db
python3 main.py
```

---

## Améliorations futures possibles

### Fonctionnalités
- [ ] Système de tags/catégories pour les tâches
- [ ] Filtres et recherche avancée
- [ ] Tri personnalisable (par date, statut, priorité)
- [ ] Export/Import des tâches (JSON, CSV)
- [ ] Rappels et notifications
- [ ] Mode sombre / personnalisation des thèmes
- [ ] Sous-tâches et dépendances entre tâches

### Technique
- [ ] Tests unitaires (pytest)
- [ ] Tests d'intégration
- [ ] CI/CD avec GitHub Actions
- [ ] Packaging (PyInstaller, py2app)
- [ ] Migration vers PostgreSQL pour multi-utilisateurs
- [ ] API REST pour synchronisation cloud
- [ ] Application mobile compagnon

---

## Auteur

**Isaac Marshall** - Étudiant M2 Fullstack - MyDigitalSchool

---

## Licence

Ce projet est un projet pédagogique dans le cadre du M2 Fullstack à MyDigitalSchool.

---