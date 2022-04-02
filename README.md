<p align="center">
  <img width="400" height="400" alt="Backtracking" src="https://user-images.githubusercontent.com/81054281/161360142-48b0d3ac-4f8d-492b-9784-c807cded6dac.png">
</p>



<h1 align="center">Trabalho prático - Teoria e Modelo de Grafos</h1>

<p align="center">Implementar uma biblioteca para manipular grafos não direcionados ponderados </p>

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=FINALIZADOO&color=GREEN&style=for-the-badge)


## Descrição do Projeto

O objetivo do trabalho é projetar e implementar uma biblioteca para manipular grafos não direcionados ponderados. As ponderações são valores reais que devem estar associados às arestas do grafo. A biblioteca deve ser capaz de representar grafos não direcionados ponderados e de fornecer um conjunto de algoritmos em grafos. Deve-se projetar e desenvolver a biblioteca de forma que ela possa ser facilmente utilizada em outros programas.


<div align="center">
   <img width="400" height="400" alt="Grafo" src="https://user-images.githubusercontent.com/81054281/161362835-609372f2-1380-4bb9-a323-4e1f91d81706.png">
   <img width="300" height="400" alt="Entradas" src="https://user-images.githubusercontent.com/81054281/161362957-ee499087-a690-4aef-be48-06618f510ca4.png"/>
</div>

Entrada de dados: A biblioteca deve ser capaz de ler um grafo de um arquivo texto. O formato do grafo no arquivo será o seguinte: a primeira linha informa o número de vértices do grafo, cada linha subsequente informa as arestas com seu respectivo peso

## ✔️ Técnicas e tecnologias utilizadas

- ``Linguagem de programação Python``
- ``Visual Studio Code (VS Code)``

## 🔨 Funcionalidades principais do projeto

- Ordem do grafo
- Tamanho do grafo
- Densidade ε(G) do grafo
- Os vizinhos de um vértice fornecido
- Grau de um vértice fornecido
- Verificar se um vértice é articulação
- Determinar a sequência de vértices visitados na busca em largura e informar a(s) aresta(s) que não faz(em) parte da árvore de busca em largura.
- Determinar o número de componentes conexas do grafo e os vértices de cada componente (Algoritmo de Roy)
- Verificar se um grafo possui ciclo.
- Determinar distância e caminho mínimo
  - Sua biblioteca deve ser capaz de calcular a distância e caminho mínimo entre um dado vértice e todos os outros vértices do grafo.
- Determinar a árvore geradora mínima de um grafo.
    - A árvore geradora mínima deve ser escrita em um arquivo (no mesmo formato de entrada do grafo), assim como seu peso total.
- Verificar se um grafo é euleriano. Em caso afirmativo, determinar uma cadeia euleriana fechada (Algoritmo de Fleury).
- Por fim, em https://paad-grafos.herokuapp.com pode-se salvar o grafo num arquivo .json. Uma rotina que leia o arquivo .json e o coloque no formato de entrada exigido pelo arquivo de entrada deste trabalho. Além disso, uma rotina que pegue um arquivo texto no formato de entrada exigido neste trabalho e gere o arquivo .json de modo que seja importado para o https://paad-grafos.herokuapp.com
