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

## Explications détaillées

### Architecture et conception

#### Pourquoi séparer Modèle, Vue et Contrôleur ?

L'architecture **MVC** est un patron de conception qui a fait ses preuves depuis des décennies. Dans ce projet, chaque couche a une responsabilité bien définie :

**Le Modèle (`models/`)** est la **source de vérité** :
- Il ne connaît rien de l'interface graphique
- Il gère uniquement les données et leur persistance
- Il contient toute la logique métier (validation, calculs, règles)
- Si demain on décide de créer une API REST ou une interface en ligne de commande, on réutilise le même modèle sans modification

**La Vue (`views/`)** est **passive et déclarative** :
- Elle affiche simplement ce qu'on lui dit d'afficher
- Elle émet des signaux quand l'utilisateur interagit (clic, saisie, etc.)
- Elle ne prend aucune décision métier
- Elle ne sait pas comment les données sont stockées

**Le Contrôleur (`controllers/`)** est le **chef d'orchestre** :
- Il écoute les signaux de la Vue
- Il interroge ou met à jour le Modèle en conséquence
- Il demande à la Vue de se mettre à jour après une modification
- Il contient la logique de navigation (ouvrir une vue détail, revenir à la liste, etc.)

**Exemple concret** : Quand tu cliques sur "Ajouter une tâche"
1. La **Vue** émet un signal `clicked` (elle ne sait rien de ce qui va se passer)
2. Le **Contrôleur** reçoit le signal, récupère les données des champs de saisie
3. Le **Contrôleur** demande au **Modèle** : "Crée une tâche avec ces infos"
4. Le **Modèle** valide les données, les insère en base, retourne la tâche créée
5. Le **Contrôleur** demande à la **Vue** : "Affiche cette nouvelle tâche dans la liste"

Cette séparation permet de **tester facilement** : on peut tester le Modèle sans interface, tester le Contrôleur avec un faux Modèle, etc.

---

### Le système Signal/Slot de Qt

Qt utilise un mécanisme puissant appelé **Signal/Slot** qui remplace les callbacks traditionnels. C'est un système événementiel typé et sécurisé.

#### Qu'est-ce qu'un Signal ?
Un **signal** est un événement émis par un widget quand quelque chose se passe. Par exemple :
- `clicked` quand on clique sur un bouton
- `textChanged` quand le contenu d'un champ texte change
- Des signaux personnalisés que tu définis toi-même (comme `edit_clicked` dans `TaskRowWidget`)

#### Qu'est-ce qu'un Slot ?
Un **slot** est une fonction Python ordinaire qui réagit à un signal. Quand un signal est émis, tous les slots connectés sont appelés automatiquement.

#### Exemple pratique
```python
# Dans TaskRowWidget, on définit nos propres signaux
class TaskRowWidget(QWidget):
    edit_clicked = Signal(int)      # Signal personnalisé qui transmet un ID
    delete_clicked = Signal(int)
    
    def __init__(self, task):
        # ...
        edit_btn.clicked.connect(
            lambda: self.edit_clicked.emit(self.task["id"])
        )
```

```python
# Dans MainWindow, on connecte ce signal à une action
widget.edit_clicked.connect(
    lambda id: self.parent_controller.open_task_detail(id)
)
```

**Ce qui se passe** :
1. Utilisateur clique sur le bouton ✏️
2. Signal `clicked` du bouton → appelle le lambda
3. Lambda émet le signal `edit_clicked` avec l'ID de la tâche
4. Signal `edit_clicked` → appelle `open_task_detail()` dans le contrôleur
5. Le contrôleur ouvre la vue détail

**Avantage majeur** : Les widgets ne se connaissent pas entre eux. Le `TaskRowWidget` ne sait pas qu'il y a un contrôleur, il émet juste un signal. C'est le code parent qui décide quoi faire avec ce signal.

---

### Gestion de la persistance avec SQLite

#### Pourquoi SQLite et pas un simple fichier JSON ?

**SQLite offre plusieurs avantages** :
- **Transactions ACID** : si l'app crash pendant une écriture, la base reste cohérente
- **Requêtes SQL** : filtrer, trier, rechercher devient trivial
- **Index** : performances même avec des milliers de tâches
- **Concurrent access** : gestion automatique des accès simultanés
- **Standard** : tous les langages ont des drivers SQLite

**Avec un fichier JSON**, tu devrais :
- Lire tout le fichier en mémoire
- Modifier la structure Python
- Réécrire tout le fichier (risque de corruption si l'app crash)
- Pas de requêtes : tu dois parcourir toutes les tâches pour filtrer

#### Organisation de la couche base de données

```python
# database.py - Point d'entrée unique pour la connexion
def get_connection():
    conn = sqlite3.connect('data/tasks.db')
    conn.row_factory = sqlite3.Row  # Permet d'accéder par nom de colonne
    return conn
```

```python
# task_model.py - Toutes les opérations sur les tâches
class TaskModel:
    def create_task(self, title, description):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (title, description, status)
            VALUES (?, ?, 'À faire')
        """, (title, description))
        conn.commit()
        # ...
```

**Pourquoi des méthodes dédiées ?**
- Chaque opération CRUD est testable individuellement
- Le SQL est centralisé (pas éparpillé dans toute l'app)
- Si on change de base (PostgreSQL), on modifie juste ce fichier

---

### Le Dark Mode : Comment ça fonctionne ?

Le dark mode utilise trois mécanismes Qt :

#### 1. QSettings pour la persistance
```python
self.settings = QSettings("TaskManager", "DarkMode")
self.dark_mode = self.settings.value("dark_mode", False, type=bool)
```

`QSettings` stocke les préférences utilisateur dans l'emplacement standard de l'OS :
- **macOS** : `~/Library/Preferences/com.TaskManager.DarkMode.plist`
- **Windows** : Registre Windows
- **Linux** : `~/.config/TaskManager/DarkMode.conf`

#### 2. Feuilles de style dynamiques (QSS)
Qt utilise un système de styles CSS-like appelé **QSS (Qt Style Sheets)** :

```python
def apply_theme(self):
    if self.dark_mode:
        self.setStyleSheet(self.get_dark_stylesheet())
    else:
        self.setStyleSheet(self.get_light_stylesheet())
```

Les feuilles de style peuvent cibler :
- Des types de widgets : `QPushButton { ... }`
- Des IDs spécifiques : `QPushButton#dark_mode_btn { ... }`
- Des états : `QPushButton:hover { ... }`

#### 3. Propagation du thème
Quand on bascule le mode, il faut mettre à jour **tous** les widgets :

```python
def toggle_dark_mode(self):
    self.dark_mode = not self.dark_mode
    self.apply_theme()  # Applique à la fenêtre principale
    
    # Met à jour chaque widget de tâche existant
    for i in range(self.task_list.count()):
        widget = self.task_list.itemWidget(self.task_list.item(i))
        widget.apply_theme(self.dark_mode)
```

**Pourquoi passer `dark_mode` en paramètre aux widgets ?**
```python
widget = TaskRowWidget(task, self.dark_mode)
```

Parce que les widgets enfants doivent connaître le thème actif dès leur création. Sinon, une nouvelle tâche ajoutée en mode sombre apparaîtrait en mode clair.

---

### Gestion des images de bannière

Les images sont stockées localement dans un dossier `images/` avec une convention de nommage :

```python
image_filename = f"task_{self.task['id']}_banner.png"
dest_path = os.path.join("images", image_filename)
```

**Étapes de l'upload** :
1. Utilisateur sélectionne une image via `QFileDialog`
2. L'image est copiée dans `images/task_X_banner.png`
3. L'image est redimensionnée avec Pillow (évite les fichiers trop lourds)
4. Le chemin est stocké en base dans `image_path`
5. L'aperçu est mis à jour avec `QPixmap`

**Pourquoi pas stocker l'image en base (BLOB) ?**
- Plus simple de gérer des fichiers
- Les OS optimisent le cache des fichiers
- Plus facile de faire des backups
- Pas de limite de taille en base

**Gestion de la suppression** :
```python
def clear_banner(self):
    if os.path.exists(self.task["image_path"]):
        os.remove(self.task["image_path"])
    self.task["image_path"] = None
```

---

### Widgets personnalisés

#### TaskRowWidget : Un widget réutilisable

Au lieu de gérer chaque ligne de tâche manuellement, on crée un **widget personnalisé** qui encapsule :
- L'affichage (label, boutons, combo de statut)
- Le comportement (signaux pour édition/suppression)
- Le style (hover, couleurs)

**Avantages** :
- **Réutilisable** : on crée une fois, on utilise partout
- **Maintenable** : le code de la ligne est isolé
- **Testable** : on peut tester le widget indépendamment

```python
class TaskRowWidget(QWidget):
    # Définir des signaux personnalisés
    edit_clicked = Signal(int)
    delete_clicked = Signal(int)
    
    def __init__(self, task, dark_mode=False):
        # Construire l'UI du widget
        # Connecter les signaux internes
```

**Utilisation** :
```python
widget = TaskRowWidget(task, self.dark_mode)
self.task_list.setItemWidget(item, widget)
widget.edit_clicked.connect(self.handle_edit)
```

---

### Navigation entre vues avec QStackedWidget

Le `QStackedWidget` permet d'avoir plusieurs "pages" dans la même fenêtre :

```python
self.stack = QStackedWidget()
self.stack.addWidget(self.page_main)      # Index 0
self.stack.addWidget(self.detail_view)    # Index 1
self.stack.setCurrentIndex(1)             # Affiche la vue détail
```

**Avantage vs ouvrir une nouvelle fenêtre** :
- Une seule fenêtre = UX plus fluide
- Pas de gestion de fenêtres multiples
- Transitions plus rapides

**Gestion du parent Qt** :
```python
detail_view = TaskDetailView(task, parent=self.view.stack)
```

Le `parent` est crucial en Qt :
- Qt détruit automatiquement les enfants quand le parent est détruit
- Évite les fuites mémoire
- Évite l'erreur "Internal C++ object already deleted"

---

### Gestion des erreurs et validation

#### Validation côté Modèle
```python
def create_task(self, title, description):
    if not title or not title.strip():
        raise ValueError("Le titre est obligatoire")
    # ...
```

Le modèle **refuse** les données invalides. C'est lui le gardien de l'intégrité.

#### Affichage côté Vue
```python
try:
    new_task = self.model.create_task(title, desc)
    self.view.add_task_to_list(new_task)
except ValueError as e:
    self.view.show_error(str(e))
```

Le contrôleur capture l'erreur et demande à la vue de l'afficher.

**Pourquoi ne pas valider dans la Vue ?**
Parce que la Vue ne devrait pas connaître les règles métier. Si demain on dit "le titre doit faire minimum 3 caractères", on modifie juste le Modèle, pas la Vue.

---

### Astuces et bonnes pratiques appliquées

#### 1. Horodatage automatique
```sql
created_at TEXT DEFAULT CURRENT_TIMESTAMP
updated_at TEXT DEFAULT CURRENT_TIMESTAMP
```

SQLite gère automatiquement les dates de création et modification.

#### 2. Conversion Row → dict
```python
conn.row_factory = sqlite3.Row
# ...
task = dict(cursor.fetchone())
```

`sqlite3.Row` permet d'accéder aux colonnes par nom, et `dict()` convertit en dictionnaire Python standard.

#### 3. Paramètres SQL préparés
```python
cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
```

**Toujours** utiliser des paramètres préparés (`?`) au lieu de concaténer des strings. Cela prévient les injections SQL.

#### 4. Context manager pour la connexion
```python
with get_connection() as conn:
    cursor = conn.cursor()
    # ...
    conn.commit()
```

Le `with` garantit que la connexion est fermée même en cas d'erreur.

---

### Limitations actuelles et pistes d'amélioration

#### Ce qui pourrait être amélioré

**1. Tests unitaires**
Actuellement, le code n'a pas de tests automatisés. Ajouter des tests avec `pytest` permettrait de :
- Vérifier que le Modèle gère bien les cas limites
- Tester les validations
- Éviter les régressions lors de modifications

**2. Gestion des erreurs réseau (futur)**
Si on ajoute une synchronisation cloud, il faudra gérer :
- Les timeouts
- Les conflits de version
- Le mode hors-ligne

**3. Performance avec beaucoup de tâches**
Actuellement, toutes les tâches sont chargées en mémoire. Avec 10 000 tâches, il faudrait :
- Pagination
- Lazy loading
- Virtualisation de la liste

**4. Undo/Redo**
Implémenter un système de Command Pattern pour annuler/refaire les actions.

---

## 🐛 Résolution de problèmes

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