# exercice1.py
from datetime import datetime
import json
from abc import ABC, abstractmethod

class Horodatable:
    def horodatage(self):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"[LOG] Action à {ts}")
        if hasattr(self, "enregistrer"):
            self.enregistrer(f"horodatage: {ts}")

class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")
        print("Validation OK")
        if hasattr(self, "enregistrer"):
            self.enregistrer("validation: OK")

class Historisable:
    def __init__(self, *args, **kwargs):
        self._historique = []
        super().__init__(*args, **kwargs)
    def enregistrer(self, action):
        ts = datetime.now().isoformat()
        self._historique.append({"action": action, "timestamp": ts})
    def get_historique(self):
        return list(self._historique)

class Serializable(ABC):
    @abstractmethod
    def to_json(self):
        pass

class Document(Horodatable, Validable, Historisable, Serializable):
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu
        super().__init__()
    def sauvegarder(self):
        self.horodatage()
        self.valider()
        if hasattr(self, "enregistrer"):
            self.enregistrer("sauvegarde")
        print(f"Document '{self.titre}' sauvegardé.")
    def to_json(self):
        data = {"titre": self.titre, "contenu": self.contenu, "historique": self.get_historique()}
        return json.dumps(data, ensure_ascii=False, indent=2)


