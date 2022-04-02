from Classes.Grafo import Grafo
file = str(input("Nome do arquivo:"))
file = file + ".txt"
grafo = Grafo(file)

while(True):
    print()
    print("===========================")
    print("===========MENU============")
    print("===========================")
    print("Escolha uma opção abaixo:")
    print("[1] Ordem do grafo")
    print("[2] Tamanho do grafo")
    print("[3] Densidade do grafo")
    print("[4] Os vizinhos de um vertice")
    print("[5] Grau do vertice")
    print("[6] Verificar se o verfice é articulação")
    print("[7] Sequência de vértices visitados e não visitados na busca em largura")
    print("[8] Número de componentes conexas e os vértices de cada componente")
    print("[9] Verificar se o grafo é um circulo")
    print("[10] Determinar a distancia e caminho mínimo")
    print("[11] Arvore geradora mínima do grafo")
    print("[12] Verificar se é um grafo euleriano.")
    print("[0]Sair")
    cod = int(input("Insira o código:"))
    
    if(cod == 0):
        break
    if(cod==1):
        print(f"Ordem do grafo:{grafo.getOrdem()}")
    elif(cod==2):
        print(f"Tamanho do grafo:{grafo.getTamanho()}")
    elif(cod==3):
        print(f"Desidade do grafo:{grafo.getDensidade()}")
    elif(cod==4):
        vertice = int(input("Insira o vertice que deseja consultar os vizinhos:"))
        vizinhos = grafo.getVizinho(vertice)
        print("Vizinhos:",end="")
        for i in range(len(vizinhos)):
            print(f"{vizinhos[i]} ",end="")
        print()
    elif(cod == 5):
        vertice = int(input("Insira o vertice que deseja consultar o grau:"))
        print(f"O grau do vertice {vertice} é {grafo.getGrau(vertice)}")
    elif(cod == 6):
        vertice = int(input("Insira o vertice que deseja consultar se é uma articulação:"))
        if(grafo.isArticulacao(vertice) == True):
            print("É uma articulação.")
        else:
            print("Não é uma articulação")
    elif(cod == 7):
        verticesVisitados, verticesNVisitados = grafo.buscaLargura()
        print(f"Sequencia de vertices visitados na busca em largura:")
        for i in range(len(verticesVisitados)):
            print(f"{verticesVisitados[i]} ",end="")
        print()
        print(f"Sequencia de não vertices visitados na busca em largura:")
        for i in range(len(verticesNVisitados)):
            for j in range(len(verticesNVisitados[i])):
                print(f"{verticesNVisitados[i][j]} ",end="")
        print()
    elif(cod == 8):
        quantComponentesConexas,verticeComponentes = grafo.calculaComponentesConexas()
        print(f"Número de componentes conexas:{quantComponentesConexas}")
        print(f"Os vertices de cada componentes:")
        for j in range(len(verticeComponentes)):
            for i in range(len(verticeComponentes[j])):
                print(f"{verticeComponentes[j][i]} ", end="")
        print("")
    elif(cod == 9):
        if(grafo.haveCicle() == True):
            print("Grafo possui circulo.")
        else:
            print("Grafo não possui circulo.")
  
    elif(cod == 10):
        vertice = int(input("Digite o vertice:"))
        menorD, caminho = grafo.menorDistancia(vertice) 
        print(grafo.menorDistancia(vertice))
        for i in range(len(menorD)):
            print(f"Distancia: {menorD[i]} | Caminho:", end="")
            if (len(caminho[i]) != 0):
                for j in range(len(caminho[i])):
                    print(f"{caminho[i][j]} ", end="")
                print()
            else:
                print("Sem caminho")
        print()
    elif(cod == 11):
        listaVertices,PesoTotal = grafo.arvoreGeradoraMinima()
        for vertices in listaVertices:
            print(f'{vertices[0]}->{vertices[1]} ||| Peso = {vertices[2]}')

        print(f"Peso total = {PesoTotal}")

    elif(cod == 12):
        grafo.fleuryF()

    else:
        print("Opção inválida.Tentar novamente!")
       







