from grafo import Grafo
from Interface.mainInterface import interface

g = []
grafo = Grafo()
#omeArquivo = input("Digite o nome do arquivo:")
grafo.inicializarGrafo("grafoTP.txt")
print(grafo.ford_Moore_Bellman(4))

#print(grafo.calculaComponentesConexas())

