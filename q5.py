'''
Crie um grafo vazio. Peça para o usuário digitar os vértices e as arestas desse grafo. O usuário deve informar
os pares de vértices que formam cada aresta.'''

grafo = {}

num_vertices = int(input('Informe o número de vértices do grafo: '))
for i in range(num_vertices):
    vertice = input('Digite o nome do vértice: ')
    grafo[vertice] = []
   
num_arestas = int(input('Informe o número de arestas do grafo: '))
for i in range(num_arestas):
    a, b = input(f'Digite os vértices que formam a aresta {i+1}: ').split()
    grafo[a].append(b)
    grafo[b].append(a)
   
print(grafo)
