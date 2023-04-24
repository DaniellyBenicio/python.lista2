'''Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. 
O usuário deve informar os pares de vértices que formam cada aresta. 
Em seguida, peça para o usuário escolher uma das arestas e removê-la do grafo.'''

grafo = {}

numVertices = int(input('Informe o número de vértices do grafo: '))
for i in range(numVertices):
    vertice = input('Digite o nome do vértice: ')
    grafo[vertice] = []
    
numArestas = int(input('Informe o número de arestas do grafo: '))
for i in range(numArestas):
    a, b = input(f'Digite os vértices que formam a aresta {i+1}: ').split()
    grafo[a].append(b)
    grafo[b].append(a)

print(grafo)

a, b = input('Qual aresta deseja remover do grafo? ').split()

if a in grafo and b in grafo:
    grafo[a].remove(b)
    grafo[b].remove(a)
    print('Aresta removida do grafo!')
    print(grafo)
else:
    print('A aresta não foi encontrada no grafo!')
