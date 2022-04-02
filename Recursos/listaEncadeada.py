class NodoLista:
    def __init__(self, dado = 0, nodeprox = None):
        self.dado = dado
        self.proximo = nodeprox

    def imprimeNode(self):
        print(self.dado, end=" ")

class ListaEncadeada(object):
    def __init__(self):
        self.cabeca = None
    
    def inserir(self, dado):
        if self.cabeca:
            ponteiro = self.cabeca
            while(ponteiro.proximo):
                 ponteiro = ponteiro.proximo
            ponteiro.proximo = NodoLista(dado=dado)
        else: 
           self.cabeca = NodoLista(dado=dado) 

    def imprimeLista(self):
        ponteiro = self.cabeca
        while(ponteiro != None):
            ponteiro.imprimeNode()
            ponteiro = ponteiro.proximo





