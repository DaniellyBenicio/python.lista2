'''Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. O usuário deve informar os 
pares de vértices que formam cada aresta. Em seguida, verifique se a aresta ('A', 'C') está presente no grafo.'''

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

if 'A' in grafo['C']:
    print('Aresta ("AC") presente no grafo!')
else:
    print('Aresta não está presente no grafo!')