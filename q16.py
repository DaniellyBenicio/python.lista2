'''Peça para o usuário digitar 10 números e crie uma lista com esses números. 
Em seguida, multiplique cada elemento da lista por 2 e crie uma nova lista com esses valores.'''

lista = []

for i in range(0, 10):
    num = int(input(f'Digite o {i+1}º número: '))
    lista.append(num)
print(lista)

novaLista = []

for num in lista:
    novaLista.append(num * 2)
print(novaLista)
