from database.DAO import DAO
import networkx as nx
from datetime import datetime

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMapFermate = {}
        for u in self._fermate:
            self._idMapFermate[u.id_fermata] = u

    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)

        #tic = datetime.now()
        #self.addedges()
        #toc = datetime.now()
        #print("tempo impiegato da modo 1: ", toc-tic)

        #tic = datetime.now()
        #self.addedges2()
        #toc = datetime.now()
        #print("tempo impiegato da modo 2: ", toc - tic)

        tic = datetime.now()
        self.addedges3()
        toc = datetime.now()
        print("tempo impiegato da modo 3: ", toc - tic)

    def addedges(self):
        self._grafo.clear_edges()
        for u in self._fermate:
            for v in self._fermate:
                if DAO.hasconn(u,v):
                    self._grafo.add_edge(u, v)


    def addedges2(self):
        self._grafo.clear_edges()
        for u in self._fermate:
            for conn in DAO.getvicini(u):
                v = self._idMapFermate[conn.id_stazA]
                self._grafo.add_edge(u, v)

    def addedges3(self):
        self._grafo.clear_edges()
        alledges = DAO.getAllEdges()
        for conn in alledges:
            u = self._idMapFermate[conn.id_stazP]
            v = self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)

    #QUESTI 4 METODI SONO TUTTI EQUIVALENTI, CAMBIA SOLO IL METODO DI RAPPRESENTAZIONE, DA ARCHI O DA ALBERO
    def getBFSNodesFromEdges(self,source):
        archi = nx.bfs_edges(self._grafo,source)
        nodiBFS = []
        for u, v in archi:
            nodiBFS.append(v)
        return nodiBFS

    def getBFSNodesFromTree(self,source):
        tree = nx.bfs_tree(self._grafo,source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi


    def getDFSNodesFromEdges(self, source):
        archi = nx.dfs_edges(self._grafo, source)
        nodiDFS = []
        for u, v in archi:
            nodiDFS.append(v)
        return nodiDFS

    def getDFSNodesFromTree(self, source):
        tree = nx.dfs_tree(self._grafo, source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi




    def get_numnodi(self):
        return len(self._grafo.nodes())

    def get_numarchi(self):
        return len(self._grafo.edges())

    @property
    def fermate(self):
        return self._fermate