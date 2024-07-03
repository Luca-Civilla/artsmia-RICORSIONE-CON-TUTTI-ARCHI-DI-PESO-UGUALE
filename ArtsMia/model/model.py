import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.ruoli = DAO.getAllRoles()
        self._grafo = nx.Graph()
        self._bestPath = []
        self._bestScore = 0#INDICA LUNGHEZZA DEL PERCORSO
        self.pesoArco = 0
    def getPath(self,nodo):
        self._bestPath = []
        self._bestScore = 0
        self.pesoArco = 0#INIZIALIZZO IL PESO DELL'ARCO CHE POI DOVRA0 ESSERE RISPETTATO PER TUTTA LA RICORSIONE
        parziale = [nodo]#IL PERCORSO DEVE INIZIARE DALL'ARTISTA CHE VIENE PASSATO

        for vicino in self._grafo.neighbors(nodo):
            parziale.append(vicino)
            self.pesoArco= self._grafo[nodo][vicino]["weight"]
            self._ricorsione(parziale,self.pesoArco)
            parziale.pop()
        return self._bestPath, self._bestScore,self.pesoArco


    def _ricorsione(self,parziale, pesoArco):#IL CAMMINO DEVE ESSERE PIU' LUNGO, NEL SENSO DI NUMERO DI VERTICI ATTRAVERSATI
        #CONDIZIONE FINALE
        if len(parziale)>self._bestScore:#SE TROVO UN PARZIALE CON LUNGHEZZA MAGGIORE DEL VALORE ATTUALE AGGIORNO
            self._bestScore = len(parziale)
            self._bestPath = copy.deepcopy(parziale)
            #NON E' UNA CONDIZIONE PER TERMINARE PERCHE' POSSO ANCORA AGGIUNGERE VERTICI VICINI

        for vicino in self._grafo.neighbors(parziale[-1]):
            if vicino not in parziale:#VERIFICO CHE IL VICINO NON SIA GIA' PRESENTE PER EVITARE CICLI
                if self._grafo[parziale[-1]][vicino]["weight"] == pesoArco:#VERIFICO CHE IL PESO SIA UGUALE A QUELLO PASSATO
                    parziale.append(vicino)
                    self._ricorsione(parziale,pesoArco)
                    parziale.pop()



    def buildGraph(self,ruolo):
        self._grafo.clear()
        self.artisti = DAO.getVertici(ruolo)
        self._grafo.add_nodes_from(self.artisti)
        self.creaArchi()


    def creaArchi(self):
        self._grafo.clear_edges()
        for u in self._grafo.nodes:
            for v in self._grafo.nodes:
                if u != v:
                    result = DAO.getArchi(u.artist_id,v.artist_id)
                    if result[0]>0:
                        peso = int(result[0])
                        self._grafo.add_edge(u,v,weight= peso)

    def Connessi(self):
        lista = []
        archi = self._grafo.edges(data=True)
        for a in archi:
            lista.append(a)
        lista.sort(key=lambda x:x[2]["weight"], reverse=True)
        return lista



    def graphDetails(self):
        return len(self._grafo.nodes),len(self._grafo.edges)