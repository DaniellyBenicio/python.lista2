'''Crie uma lista vazia e peça para o usuário digitar 10 números. 
Em seguida, retorne os elementos de índice par da lista.'''

lista = []

for i in range(0, 10):
    num = int(input(f'Digite {i}º número do índice: '))
    lista.append(num)

for i in range(len(lista)):
    if i % 2 == 0:
        print(lista[i])
