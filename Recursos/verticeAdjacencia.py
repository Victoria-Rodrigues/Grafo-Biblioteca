from Recursos.listaEncadeada import ListaEncadeada

class VerticeAdjacencia:
    def __init__(self, vertice):
        self.lista = ListaEncadeada()
        self.vertice = vertice
    
    def insereNaLista(self, vizinho):
        self.lista.inserir(vizinho)

    def imprimirVerticeAdejacencia(self):
        print(f"{self.vertice} ->", end=" ")
        self.lista.imprimeLista()
        
