'''Peça para o usuário digitar 5 números e crie uma lista com esses números. 
Em seguida, peça para o usuário digitar mais um número e adicione esse número à lista
'''

lista = []

for i in range (1,6):
    num = int(input(f'Digite {i}º número: '))
    lista.append(num)

n = int(input(f'Digite mais um número: '))
lista.append(n)

print('Números da lista: ', lista)
