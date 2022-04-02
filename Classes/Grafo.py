from math import inf

from numpy import true_divide
from Classes.Aresta import Aresta
from Classes.Vertice import Vertice
from Classes.arvoreLargura import TreeWidth
import json
from Classes.fleury import Fleury
import random

class Grafo:
    def __init__(self,nomeArquivo):
        self.vertices = []
        self.arestas = []
        self.dadosArquivo = list()

        if(nomeArquivo == None):
            print("Nome de arquivo é NoneType")
            return
        elif('json' in nomeArquivo):
            with open("Arquivos/"+nomeArquivo, encoding='utf-8') as meu_json:
                dados = json.load(meu_json)
            self.ordem = int(dados["data"]["nodes"]["length"])
            self.fleury = Fleury(self.ordem)
            for i in range(self.ordem):
                self.vertices.append(Vertice(int(dados["data"]["nodes"]["_data"][str(i+1)]['id'])))
            self.matrizValores = [[0 for i in range(self.ordem)] for j in range(self.ordem)]
            self.matrizAdjacencia = [[0 for i in range(self.ordem)] for j in range(self.ordem)]
            for i in range(dados["data"]["edges"]["length"]):
                linha = dados["data"]["edges"]["_data"][str(i+1)]
                self.arestas.append(Aresta(linha["from"],linha["to"],linha["label"],i+1))
                self.vertices[int(linha["from"]) - 1].somaGrau()
                self.vertices[int(linha["to"]) - 1].somaGrau()
                self.vertices[int(linha["from"]) - 1].adicionaVizinho(linha["to"])
                self.vertices[int(linha["to"]) - 1].adicionaVizinho(linha["from"])
                self.matrizValores[int(linha["from"]) - 1][int(linha["to"]) - 1] += float(linha["label"])
                self.matrizValores[int(linha["from"]) - 1][int(linha["to"]) - 1] += float(linha["label"])
                self.matrizAdjacencia[int(linha["from"]) - 1][int(linha["to"]) - 1] += 1
                self.matrizAdjacencia[int(linha["from"]) - 1][int(linha["to"]) - 1] += 1
                self.dadosArquivo.append((linha["from"], linha["to"], linha["label"]))
                self.fleury.adicionarAresta(int(linha["from"] - 1), int(linha["to"] - 1))

            self.tamanho = dados["data"]["edges"]["length"]
        else:
            arquivo = open('Arquivos/'+nomeArquivo,"r").readlines()
            self.ordem = int(arquivo[0].replace('\n',""))
            self.fleury = Fleury(self.ordem)
            for i in range(self.ordem):
                self.vertices.append(Vertice(i+1))
            self.matrizValores = [[0 for i in range(self.ordem)] for j in range(self.ordem)]
            self.matrizAdjacencia = [[0 for i in range(self.ordem)] for j in range(self.ordem)]
            for i in range(1,len(arquivo)):
                linha = arquivo[i].split()
                self.arestas.append(Aresta(linha[0],linha[1],linha[2],i))
                self.vertices[int(linha[0]) - 1].somaGrau()
                self.vertices[int(linha[1]) - 1].somaGrau()
                self.vertices[int(linha[0]) - 1].adicionaVizinho(linha[1])
                self.vertices[int(linha[1]) - 1].adicionaVizinho(linha[0])
                self.matrizValores[int(linha[0]) - 1][int(linha[1]) - 1] += float(linha[2])
                self.matrizValores[int(linha[1]) - 1][int(linha[0]) - 1] += float(linha[2])
                self.matrizAdjacencia[int(linha[0]) - 1][int(linha[1]) - 1] += 1
                self.matrizAdjacencia[int(linha[1]) - 1][int(linha[0]) - 1] += 1
                self.fleury.adicionarAresta(int(linha[0])-1,int(linha[1])-1)
                self.dadosArquivo.append((linha[0], linha[1], linha[2]))

            self.tamanho = len(arquivo)-1


    def getOrdem(self):
        return self.ordem

    def getTamanho(self):
        return self.tamanho

    def getDensidade(self):
        return self.tamanho/self.ordem

    def getVizinho(self,vertice):
        return self.vertices[vertice-1].getVizinhos()

    def getGrau(self,vertice):
        return self.vertices[vertice-1].getGrau()

    def isArticulacao(self,vertice):
        aux = self.matrizAdjacencia
        for i in range(self.ordem):
            if aux[i][vertice - 1] != 0:
                aux[i][vertice - 1] = 0
                aux[vertice - 1][i] = 0
        vertices = []
        if vertice -1 ==0:
            vizinho = vertice +1
        else:
            vizinho = vertice -1
        self.isArticulacaoAux(vizinho,aux,vertice,vertices)
        if len(vertices) == self.ordem -1:
            return False
        else:
            return True

    def isArticulacaoAux(self,vizinho,grafo,verticeAnalise,lista):
        if vizinho not in lista:
            lista.append(vizinho)
            vizinhosGrafo = []
            for i in range(self.ordem):
              if grafo[i][vizinho-1] != 0:
                  vizinhosGrafo.append(i+1)
            for Vizinho in vizinhosGrafo:
                if Vizinho != verticeAnalise:
                    self.isArticulacaoAux(Vizinho,grafo,verticeAnalise,lista)


    def buscaLargura(self,vertice = 1):
        fila = []
        marcados = []
        marcados.append(vertice)
        fila.append(vertice)
        arvoreLargura = TreeWidth()
        arvoreLargura.start(vertice)
        verticesVisitados = []
        arestasNaoVisitadas = []
        while len(fila) != 0:
            vertice = fila[0]
            fila.pop(0)
            verticesVisitados.append(vertice)
            adjacencia = self.vertices[vertice - 1].getVizinhos()
            for vizinhos in adjacencia:
                vizinhos = int(vizinhos)
                if vizinhos not in marcados:
                    arvoreLargura.explorar(vertice,vizinhos)
                    fila.append(vizinhos)
                    marcados.append(vizinhos)
                elif arvoreLargura.areExplore(vertice,vizinhos) == False:
                    arvoreLargura.explorar(vertice,vizinhos)
                    arestasNaoVisitadas.append([vertice,vizinhos])
        return verticesVisitados,arestasNaoVisitadas

    def writeArvoreMinima(self, listaVertices, qtdVertices):
        file = open("Arquivos/ArvoreGeradoraMinima.txt", "w")
        file.write(f'{qtdVertices}\n')
        for vertice in listaVertices:
            file.write(f'{vertice[0]} {vertice[1]} {vertice[2]}\n')

        file.write(f'Peso Total = {self.pesoTotal(listaVertices)}')


    def pesoTotal(self,listaVertices):
        pesoTotal = 0
        for vertice in listaVertices:
            pesoTotal += float(vertice[2])

        return pesoTotal

    def arvoreGeradoraMinima(self):
        listaVertices = kruskall(self.ordem, self.dadosArquivo)
        self.writeArvoreMinima(listaVertices, self.ordem)
        return listaVertices,self.pesoTotal(listaVertices)

    def haveCicle(self):
        fila = []
        visitado = []
        fila.append(1)
        explorados = []
        while len(fila) != 0:
            value = fila[0]
            fila.pop(0)
            visitado.append(value)
            aD = self.vertices[value -1].getVizinhos()
            for item in aD:
                item = int(item)
                if item not in visitado:
                    fila.append(item)
                    visitado.append(item)
                    explorados.append([value,item])
                elif [value,item] not in explorados and [item,value] not in explorados:
                    return True
        return False
   

    def menorDistancia(self,vertice):
        infinito = float('inf')
        dt = [infinito for i in range(self.ordem)]
        rot = [0 for i in range(self.ordem)]
        dt[vertice - 1] = 0
        rot[vertice-1] = infinito
        aberto = [i for i in range(1,self.ordem + 1)]
        fechado = []
        caminho = [[] for i in range(self.ordem)]
        while len(aberto) > 0 :
            r = aberto[0]
            for items in aberto:
                if(dt[items - 1] < dt[r-1]):
                    r = items
            fechado.append(r)
            aberto.remove(r)
            vizinhos = []
            aux = self.vertices[r-1].getVizinhos()
            for item in aux:
                if item not in fechado:
                    vizinhos.append(item)
            for itens in vizinhos:
                itens = int(itens)
                if(dt[itens - 1] < dt[r - 1] + self.matrizValores[r-1][itens - 1]):
                    p = dt[itens - 1]
                else:
                    p = dt[r - 1] + self.matrizValores[r-1][itens - 1]
                if p < dt[itens - 1]:
                    dt[itens - 1] = p
                    dt[itens - 1] = round(dt[itens - 1],2)
                    rot[itens-1] = r
                    caminho[itens-1].append(r)
        return dt,caminho

    def calculaComponentesConexas(self):
        visited = [False for i in range(self.ordem)]
        numComponentes = 0
        subgrafos = []
        for vertice in range(self.ordem):
            if (visited[vertice] == False):
                subgrafo = []
                self.DFS(vertice, visited,subgrafo)
                subgrafos.append(subgrafo)
                numComponentes += 1
                
                 
        return numComponentes,subgrafos


    def DFS(self, vertice, visited,subgrafo):
        subgrafo.append(vertice +1)
        visited[vertice] = True
        listaAD = self.vertices[vertice].getVizinhos()
        for i in listaAD:
            i = int(i)
            if (not visited[i-1]):
                self.DFS(i-1, visited,subgrafo)
    

    def fleuryF(self):
        print("--------------------------------------------------------------------------------"
              "\nCaminho percorrido (Obs: Caso não printe o caminho, o grafo não é euleriano)")
        self.fleury.cadeiaEuleriana()

        print("--------------------------------------------------------------------------------")

        
    def toJSON(self):
        JSONreturn = {
            "data" : {
                "nodes" : {
                    "_subscribers": {
                        "*": [],
                        "add": [
                            {}
                        ],
                        "remove": [
                            {}
                        ],
                        "update": [
                            {}
                        ]
                    },
                    "_options": {},
                    "_data":{
                    },
                    "length": 0,
                    "_idProp": "id",
                    "_type": {}
                },
                "edges": {
                    "_subscribers": {
                        "*": [],
                        "add": [
                            {}
                        ],
                        "remove": [
                            {}
                        ],
                        "update": [
                            {}
                        ]
                    },
                    "_options": {},
                    "_data": {
                    },
                    "length": 0,
                    "_idProp": "id",
                    "_type": {}
                }
            },
            "options": {
                "locale": "pt-br",
                "manipulation": {
                    "enabled": False
                },
                "edges": {
                    "font": {
                        "color": "#ffffff",
                        "strokeWidth": 0,
                        "size": 18
                    }
                },
                "nodes": {
                    "color": {
                        "border": "#698B69",
                        "background": "#458B74",
                        "highlight": {
                            "border": "#698B69",
                            "background": "#4f6e4f"
                        }
                    },
                    "font": {
                        "color": "white"
                    }
                },
                "physics": {
                    "enabled": True,
                    "forceAtlas2Based": {
                        "gravitationalConstant": -50,
                        "centralGravity": 0.01,
                        "springConstant": 0.02,
                        "springLength": 100,
                        "damping": 0.4,
                        "avoidOverlap": 0
                    },
                    "maxVelocity": 50,
                    "minVelocity": 0.1,
                    "solver": "forceAtlas2Based",
                    "stabilization": {
                        "enabled": True,
                        "iterations": 1000,
                        "updateInterval": 100,
                        "onlyDynamicEdges": False,
                        "fit": True
                    },
                    "timestep": 0.5,
                    "adaptiveTimestep": True
                }
            },
            "ponderado": True,
            "ordenado": False
        }
        JSONreturn["data"]["nodes"]["length"] = len(self.vertices)
        for items in self.vertices:
            JSONreturn["data"]["nodes"]["_data"][str(items.id)] = {
                "id" : items.id
            }
        JSONreturn["data"]["edges"]["length"] = len(self.arestas)
        for items in self.arestas:
            JSONreturn["data"]["edges"]["_data"][str(items.id)] = {
                "id" : items.id,
                "from": items.start,
                "to": items.end,
                "label": items.weight
            }
        with open("output.json","w") as f:
            json.dump(JSONreturn,f)

    def toTXT(self,nomeArquivo):
        with open("Arquivos/"+nomeArquivo, encoding='utf-8') as meu_json:
            dados = json.load(meu_json)
        with open("output.txt","w") as arquivo:
            arquivo.write(str(dados["data"]["nodes"]["length"])+"\n")
            for i in range(dados["data"]["edges"]["length"]):
                linha = dados["data"]["edges"]["_data"][str(i+1)]
                arquivo.write(str(linha["from"])+" " + str(linha["to"])+ " " + str(linha["label"])+"\n")

    

def kruskall(numeroVerticesGrafo,listaArestasTupla):

    arvoreGeradora = []
    listaFlorestas = [i for i in range(numeroVerticesGrafo)]
    listaArestasTupla.sort(key=lambda tup:tup[2]) 
    for aresta in listaArestasTupla:
        verticeOrigem = int(aresta[0]) - 1
        verticeDestino = int(aresta[1]) - 1
        if listaFlorestas[verticeOrigem] != listaFlorestas[verticeDestino]: 
            arvoreGeradora.append(aresta)
            k = listaFlorestas[verticeOrigem]
            for i in range(len(listaFlorestas)):
                if listaFlorestas[i] == k:
                    listaFlorestas[i] = listaFlorestas[verticeDestino]

    return arvoreGeradora
