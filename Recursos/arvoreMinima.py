
# 'E' como uma lista de arestas no formato (verticeOrigem,verticeDestino,peso)

def kruskall(numeroVerticesGrafo,listaArestasTupla):

    arvoreGeradora = []
    listaFlorestas = [i for i in range(numeroVerticesGrafo)]
    listaArestasTupla.sort(key=lambda tup:tup[2]) # ordena a lista de arestas pelo peso
    for aresta in listaArestasTupla:
        verticeOrigem = int(aresta[0]) - 1
        verticeDestino = int(aresta[1]) - 1
        if listaFlorestas[verticeOrigem] != listaFlorestas[verticeDestino]: #não estão na mesma árvore
            arvoreGeradora.append(aresta)
            k = listaFlorestas[verticeOrigem]
            for i in range(len(listaFlorestas)):
                if listaFlorestas[i] == k:
                    listaFlorestas[i] = listaFlorestas[verticeDestino]

    return arvoreGeradora


