from model.fermata import Fermata
from model.model import Model

model = Model()
print("numero nodi:", model.get_numnodi())
print("numero archi:",model.get_numarchi())
model.buildGraph()
print("numero nodi:", model.get_numnodi())
print("numero archi:",model.get_numarchi())


source = Fermata(2,	'Abbesses',	2.33855, 48.8843)
nodiBFS = model.getBFSNodesFromEdges(source)
print(len(nodiBFS))
for i in range(0,10):
    print(nodiBFS[i])

nodiDFS = model.getDFSNodesFromEdges(source)
print(len(nodiDFS))
for i in range(0,10):
    print(nodiDFS[i])