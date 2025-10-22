# test_tasks.py
from models.task_model import TaskModel

# On initialise le modèle
task_model = TaskModel()

# On crée quelques tâches
t1 = task_model.create_task("Découvrir PySide6", "Tester la création d'une tâche")
t2 = task_model.create_task("Faire l'interface", "Prochaine étape après le modèle")

print("Tâches créées :")
print(t1)
print(t2)

# On récupère toutes les tâches
tasks = task_model.get_all_tasks()
print("\nToutes les tâches :")
for t in tasks:
    print(f"- {t['id']}: {t['title']} ({t['status']})")

# On met à jour une tâche
updated = task_model.update_task(
    t1["id"], "Découvrir PySide6", "Modèle terminé", "En cours"
)
print("\nTâche mise à jour :", updated)

# On supprime une tâche
task_model.delete_task(t2["id"])
print("\nTâche supprimée :", t2["id"])

# Liste finale
print("\nTâches restantes :")
for t in task_model.get_all_tasks():
    print(f"- {t['id']}: {t['title']} ({t['status']})")
