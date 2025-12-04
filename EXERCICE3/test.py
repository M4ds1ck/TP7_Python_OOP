from exercice3 import Tache
t = Tache("Rapport", "Brouillon")
t.mettre_a_jour("Version 1")
t.mettre_a_jour("Version 2")
print("Description actuelle:", t.description)
print("Historique:")
t.afficher_historique()
try:
    t.titre = ""
except Exception as e:
    print("Erreur:", e)
