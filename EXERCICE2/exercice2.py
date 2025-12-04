import json
import inspect
from datetime import datetime

def _json_default(o):
    if isinstance(o, datetime):
        return o.isoformat()
    return str(o)

class Serializable:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, default=_json_default)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        params = [p for p in inspect.signature(cls.__init__).parameters.keys() if p != 'self']
        init_args = {k: data[k] for k in params if k in data}
        obj = cls(**init_args)
        for k, v in data.items():
            setattr(obj, k, v)
        return obj

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        snapshot = {k: v for k, v in self.__dict__.items() if k != 'historique'}
        self.historique.append((datetime.now(), snapshot))

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")

class Contrat(Serializable, Historisable, Journalisable):
    def __init__(self, id, description):
        Historisable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat()
        self.description = nouvelle_desc
