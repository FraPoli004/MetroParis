from model.model import Model

model = Model()
model.buildGraph()
print("numero nodi:", model.get_numnodi())
print("numero archi:",model.get_numarchi())
model.buildGraph()
print("numero nodi:", model.get_numnodi())
print("numero archi:",model.get_numarchi())