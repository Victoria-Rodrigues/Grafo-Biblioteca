from Recursos.verticeAdjacencia import VerticeAdjacencia

class ListaAdjacencia:
    def __init__(self, ordem):
        self.lista = []
        self.ordem = ordem

    def criarLista(self, grafo):
        for s in range(self.ordem):
            self.lista.append(VerticeAdjacencia(s+1))
            for i in range(self.ordem):
                if grafo[i][s] != 0: 
                    self.lista[s].insereNaLista(i+1)
        
    def obterAdjacencia(self,vertice):
        for adjacencia in self.lista:
            if adjacencia.vertice == vertice:
                return adjacencia.lista



    def imprimirListaAdjacencia(self):
        for i in range(self.ordem):
            self.lista[i].imprimirVerticeAdejacencia()
            print("\n")