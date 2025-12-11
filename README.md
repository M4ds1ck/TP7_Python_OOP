# TP7 Python – Mixins & POO Avancée 🐍

[![Python Version](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)

Ce dépôt contient les **trois exercices du TP7**, dédiés à la **Programmation Orientée Objet avancée** en Python, avec un focus particulier sur l’usage des **Mixins** pour enrichir dynamiquement les classes métier.

---

## 📂 Contenu du projet

### **EXERCICE 1 : Introduction aux Mixins**

Découverte des mixins à travers un cas simple :

* `Horodatable` → ajoute un horodatage automatique
* `Validable` → vérifie la présence d’un titre
* Classe principale `Document` utilisant les deux mixins
* Appel de `sauvegarder()` déclenchant horodatage + validation
* Script de test : `test.py`

---

### **EXERCICE 2 : Mixins avancés (Sérialisation, Historique, Journalisation)**

Modélisation d’un objet métier `Contrat` combinant trois mixins :

* `Serializable` → conversion JSON (to/from)
* `Historisable` → enregistrement des états successifs
* `Journalisable` → journal des actions en console
* Mise à jour via `modifier()` + affichage JSON

**Extensions proposées :**

* ajout d’un mixin Horodatable
* export CSV / XML
* réutilisation pour d’autres entités (Commande, Client, etc.)

---

### **EXERCICE 3 : Système de gestion des tâches**

Composition d’une classe `Tâche` avec :

* `ValidationMixin` → garantit un titre non vide
* `HistoriqueMixin` → conserve toutes les anciennes versions
* `JournalisationMixin` → journalisation de chaque action

Fonctionnalités :

* création d’une tâche avec journal
* méthode `mettre_a_jour()` (historique + log)
* méthode `afficher_historique()`
* gestion d’erreurs métier

---

## 🚀 Utilisation

1. Cloner le dépôt :

```bash
git clone https://github.com/M4ds1ck/TP7_Python_Mixins.git
```

2. Accéder à un exercice :

```bash
cd TP7_Python_Mixins/EXERCICE2
```

3. Lancer le script de test :

```bash
python test.py
```

---

## 🖥️ Exemples d’output

### Exercice 1

```bash
[LOG] Action à 2025-12-11 21:34:31.146393
Validation OK
Document 'Rapport' sauvegardé.
```

### Exercice 2

```bash
[Journal] 2025-12-11: Modification du contrat 1
{"id": 1, "description": "Révisé"}
```

### Exercice 3

```bash
[Journal] Création de la tâche 'Rapport'
[Journal] Modification de la tâche 'Rapport'
Description actuelle: Version 2
Historique:
2025-12-11 Brouillon
2025-12-11 Version 1
```

---

## 📌 Auteur

**Nom :** Mahmoud Moukouch – 2333447 – [m.moukouch2471@uca.ac.ma](mailto:m.moukouch2471@uca.ac.ma)

**GitHub :** [M4ds1ck](https://github.com/M4ds1ck)

**Projet :** TP7 Python – Mixins, Historisation & Journalisation
