'''Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
Em seguida, retorne o primeiro elemento da tupla.'''

num = []

for i in range(1, 6):
    n = int(input(f'Digite o {i}º número: '))
    num.append(n)

tup = tuple(num)

print('O primeiro valor informado: ', tup[0])

