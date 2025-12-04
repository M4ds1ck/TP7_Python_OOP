from exercice2 import Contrat
c = Contrat(1, "Initial")
c.modifier("Révisé")
print(c.to_json())
c2 = Contrat.from_json(c.to_json())
print(c2.id, c2.description)
for t, state in c.historique:
    print(t, state)
