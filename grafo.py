from cmath import inf
import random
import math
from webbrowser import get
from Recursos.arvoreLargura import TreeWidth
from Recursos.fila import Fila
from Recursos.listaAdjacencia import ListaAdjacencia
from Recursos.arvoreMinima import kruskall

class Grafo:

    def __init__(self, grafo = None, ordem = None, tamanho = None):
        self.__grafo = grafo
        self.__ordem = ordem
        self.__tamanho = tamanho
        self.dadosArquivo = list()
        self.listaAD = None
        self.nomeArquivo = None

    def inicializarGrafo(self, nomeArquivo):
        arquivo = open('Arquivos/'+nomeArquivo, "r").readlines()
        self.nomeArquivo = nomeArquivo
        self.__ordem = int(arquivo[0].replace('\n',''))
        self.__tamanho = len(arquivo)-1
        self.__grafo = [[0 for i in range(self.__ordem)] for j in range(self.__ordem)]
        for i in range(1,len(arquivo)):
            linha = arquivo[i].split()
            self.__grafo[int(linha[0]) - 1][int(linha[1]) - 1] = float(linha[2])
            self.__grafo[int(linha[1]) - 1][int(linha[0]) - 1] = float(linha[2])
            self.dadosArquivo.append((linha[0],linha[1],linha[2]))

        self.listaAD = ListaAdjacencia(self.__ordem)
        self.listaAD.criarLista(self.__grafo)

    def getMatrizRecursos(self):
        return self.__grafo

    def getOrdem(self):
        return self.__ordem
    
    def getTamanho(self):
        return self.__tamanho

    def densidade(self):
        return self.getTamanho()/self.getOrdem()
        
    def vizinhosVertice(self, vertice,grafo=None):
       lista = []
       if grafo != None:
           for i in range(self.getOrdem()):
              if grafo[i][vertice-1] != 0:
                  lista.append(i+1)

       else:
           for i in range(self.getOrdem()):
              if self.__grafo[i][vertice-1] != 0:
                  lista.append(i+1)

       return lista

    def grauVertice(self, vertice):
        cont = 0
        for i in range(self.getOrdem()):
            if self.__grafo[i][vertice-1] != 0:
                cont+=1
        return cont

    def isVerticeArticulacao(self, vertice):
        return self.verificaVertice(vertice)


    def verificaVertice(self,vertice):
        aux = self.__grafo
        for i in range(self.getOrdem()):
            if aux[i][vertice - 1] != 0:
                aux[i][vertice - 1] = 0
                aux[vertice - 1][i] = 0

        vertices = self.caminharGrafo(aux, vertice)
        if len(vertices) == self.getOrdem()-1:
            return False
        else:
            return True

    def caminharGrafo(self,grafo,vertice):
        vertices = list()
        if vertice - 1 == 0:
            self.vizinhosOfList(vertice+1,grafo,vertice,vertices)

        else:
            self.vizinhosOfList(vertice -1, grafo,vertice,vertices)

        return vertices


    def vizinhosOfList(self,vizinho,grafo,verticeAnalise,lista):
        if vizinho not in lista:
            lista.append(vizinho)
            for Vizinho in self.vizinhosVertice(vizinho,grafo):
                if Vizinho != verticeAnalise:
                    self.vizinhosOfList(Vizinho,grafo,verticeAnalise,lista)



    def BL(self, vertice):#Busca em largura
        Q = Fila()
        marcados = list()
        marcados.append(vertice)
        Q.insert(vertice)
        arvoreLargura = TreeWidth()
        arvoreLargura.start(vertice)
        verticesVizitados = list() # é uma lista que contém as combinações de posições que formam as arestas não visitadas
        arestasNaoVisitadas = list()
        while Q.tam != 0:
            V = Q.remove()
            verticesVizitados.append(V)
            aD = self.listaAD.obterAdjacencia(V)
            ponteiro = aD.cabeca
            while (ponteiro != None):
                if ponteiro.dado not in marcados:
                    arvoreLargura.explorar(V,ponteiro.dado)
                    Q.insert(ponteiro.dado)
                    marcados.append(ponteiro.dado)

                elif arvoreLargura.areExplore(V,ponteiro.dado) == False:
                    arvoreLargura.explorar(V,ponteiro.dado)
                    arestasNaoVisitadas.append([V,ponteiro.dado])

                ponteiro = ponteiro.proximo


        return verticesVizitados,arestasNaoVisitadas


    def writeArvoreMinima(self,listaVertices,qtdVertices):
        file = open("Arquivos/ArvoreGeradoraMinima.txt","w")
        file.write(f'{qtdVertices}\n')
        pesoTotal = 0
        for vertice in listaVertices:
            file.write(f'{vertice[0]} {vertice[1]} {vertice[2]}\n')
            pesoTotal += int(vertice[2])

        file.write(f'Peso Total = {pesoTotal}')

    def grafoHaveCicle(self):
        fila = Fila()
        visitado = list()
        fila.insert(1)
        explorados = list()
        # qtd = 0 serve para testar a lógica
        while fila.tam != 0:
            V = fila.remove()
            visitado.append(V)
            aD = self.listaAD.obterAdjacencia(V)
            ponteiro = aD.cabeca
            while ponteiro:
                if ponteiro.dado not in visitado:
                    fila.insert(ponteiro.dado)
                    visitado.append(ponteiro.dado)
                    explorados.append([V,ponteiro.dado])

                elif [V,ponteiro.dado] not in explorados and [ponteiro.dado,V] not in explorados:
                    return True
                    # explorados.append([V,ponteiro.dado])
                    # qtd += 1 serve para testar a lógica

                ponteiro = ponteiro.proximo

        return False
        # return qtd  serve para testar a lógica


    def arvoreGeradoraMinima(self):
        listaVertices = kruskall(self.__ordem,self.dadosArquivo)
        self.writeArvoreMinima(listaVertices,self.numeroVertices(listaVertices))

    def numeroVertices(self,listaVertices):
        listaAux = list()
        for verice in listaVertices:
            if verice[0] not in listaAux:
                listaAux.append(verice[0])

            if verice[1] not in listaAux:
                listaAux.append(verice[1])

        return len(listaAux)

    def ford_Moore_Bellman(self, vertice):
        infinito = 9999
        dt = [0 for i in range(self.getOrdem())]
        rot = {}
        dt[vertice-1] = 0

        for i in range(0, self.getOrdem()):
            if(self.__grafo[vertice-1][i] != 0):
                dt[i] = self.__grafo[vertice-1][i]
            else:
                dt[i] = infinito

        Q = Fila()
        marcados = list()
        marcados.append(vertice)
        Q.insert(vertice)
        verticesVizitados = list() # é uma lista que contém as combinações de posições que formam as arestas não visitadas
        while Q.tam != 0:
            V = Q.remove()
            verticesVizitados.append(V)
            aD = self.listaAD.obterAdjacencia(V)
            ponteiro = aD.cabeca
            while (ponteiro != None):
                if vertice != ponteiro.dado:
                    if f"{vertice}->{ponteiro.dado}" not in rot:
                        rot[f"{vertice}->{ponteiro.dado}"] = list()

                    self.pesoGrafo(ponteiro.dado-1,dt,rot,self.vizinhosVertice(ponteiro.dado),f"{vertice}->{ponteiro.dado}")

                if ponteiro.dado not in marcados:
                    Q.insert(ponteiro.dado)
                    marcados.append(ponteiro.dado)

                ponteiro = ponteiro.proximo

        print(rot) # ainda precisa de umas modificações
        return dt

    def pesoGrafo(self, vertice, dt, rot,Vizinhos,position):
        for j in range(len(Vizinhos)):
            valor = Vizinhos[j]
            if(dt[vertice] > dt[valor-1] + self.calculaPesoArco(self.__grafo, vertice, valor-1)):
                dt[vertice] = round(dt[valor-1] + self.calculaPesoArco(self.__grafo,vertice, valor-1), 2)
                if vertice != valor and valor not in rot[position]:
                    rot[position].append(valor)


    def calculaPesoArco(self, grafo, vertice1, vertice2):
        if(grafo[vertice1][vertice2] < 0): #obs acredito eu que passando uma aresta negativa tem que retornar errado mesmo
            return grafo[vertice1][vertice2]*(-1)
        return grafo[vertice1][vertice2]

    #Determinar a Distância e o caminho mínimo:
    #Não funciona para ciclos negativos
    def floyd_Washall(self):
        infinito = 9999
        R = [[0 for i in range(self.__ordem)] for j in range(self.__ordem)]
        L = self.__grafo
        for i in range(self.getOrdem()):
            for j in range(self.getOrdem()):
                if(L[i][j] == 0):
                    L[i][j] = infinito

        for i in range(self.getOrdem()):
            L[i][i] = 0 # preenchendo de 0 a diagonal principal

        for i in range(self.getOrdem()):
            for j in range(self.getOrdem()):
                if(L[i][j] == infinito):
                    R[i][j] = 0
                else:
                    R[i][j] = i
 
        for k in range(self.getOrdem()):  
            for i in range(self.getOrdem()):   
                for j in range(self.getOrdem()): 
                    if(L[i][j] > (L[i][k]+L[k][j])):
                          L[i][j] = round((L[i][k]+L[k][j]),2)
                          R[i][j] = R[k][j]       


        print("L")
        for line in L:
            print('  '.join(map(str, line)))
        print("R")
        for line in R:
            print('  '.join(map(str, line)))


    def euler(self): #verificando se todos os vertices tem grau par, O teorema de euler diz que pora um grafo se euleriano os gruas de cada vertice devem ser par
        for i in range(self.getOrdem()):
            if(self.grauVertice(i+1) % 2 == 0):
                pass
                #print(f"Vertice:{i+1}")
                #print(self.grauVertice(i+1))
            else:
                return False
        return True

    def hierholzer(self): #verifica se o grafo é Euleriano
        pass

    def fleury(self):
        if self.euler():
            vertice = random.randint(1, self.getOrdem()+1) #escolhendo um vértice qualquer do grafo
            
        else:
            return 'Nao satisfaz o teorema de Euler'
            

    def ImprimeGrafo(self):
        for line in self.__grafo:
            print('  '.join(map(str, line)))

            
    def calculaComponentesConexas(self,vertice):
         
        #inicializando todos os vertices como não visitados componentes
        visited = [False for i in range(self.getTamanho())]
       
        # armazenar o numero de componentes conexas
        numComponentes = 0
        #Para todos os vértices, verifique se um vértice não foi visitado, 
        # então execute DFS nesse vértice e incremente a contagem de variáveis ​​em 1.
        for v in range(self.getTamanho()):
            if (visited[v] == False):
                self.DFS(v, visited)
                numComponentes += 1
                 
        return numComponentes

    #O DFS visita todos os vértices conectados de um determinado vértice.
    def DFS(self, v, visited):
 
        # Marcar o componente como visitado
        visited[v] = True

        # Precorrer todos os vertices adjacente a este vertice 
        for i in self.listaAD[v]:
            if (not visited[i]):
                self.DFS(i, visited)
    

