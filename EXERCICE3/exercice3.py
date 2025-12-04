import copy
import datetime

class ValidationMixin:
    def _validate_title(self, title):
        if not title or not str(title).strip():
            raise ValueError("Le titre est obligatoire et ne peut être vide")

class HistoriqueMixin:
    def __init__(self):
        self._historique = []

    def enregistrer_historique(self, description):
        self._historique.append((datetime.datetime.now(), copy.deepcopy(description)))

    def afficher_historique(self):
        for t, desc in self._historique:
            print(t, desc)

class JournalisationMixin:
    def journaliser(self, message):
        print(f"[Journal] {datetime.datetime.now()}: {message}")

class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre, description=""):
        HistoriqueMixin.__init__(self)
        self._validate_title(titre)
        self._titre = titre
        self.description = description
        self.creation_date = datetime.datetime.now()
        self.journaliser(f"Création de la tâche '{self._titre}'")

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, value):
        self._validate_title(value)
        self._titre = value
        self.journaliser(f"Changement du titre vers '{self._titre}'")

    def mettre_a_jour(self, description):
        self.enregistrer_historique(self.description)
        self.description = description
        self.journaliser(f"Modification de la tâche '{self._titre}'")

    def afficher_historique(self):
        HistoriqueMixin.afficher_historique(self)
