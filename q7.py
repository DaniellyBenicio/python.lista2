'''Peça para o usuário digitar 5 números e crie uma tupla com esses números. 
Em seguida, retorne o primeiro elemento da tupla.'''

num = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
num4 = int(input('Digite o 4º número: '))
num5 = int(input('Digite o 5º número: '))

tup = (num, num2, num3, num4, num5)

print('O primeiro valor informado: ', tup[0])

