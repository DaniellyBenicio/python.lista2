'''Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
Em seguida, verifique quantos elementos estão no conjunto.'''

num1 = int(input(f'Digite o 1º número: '))
num2 = int(input(f'Digite o 2º número: '))
num3 = int(input(f'Digite o 3º número: '))
num4 = int(input(f'Digite o 4º número: '))
num5 = int(input(f'Digite o 5º número: '))

conj = set([num1, num2, num3, num4, num5])

print(f'O conjunto possui {len(conj)} elementos!')

'''outra forma de fazer:

conj = set()

for i in range(1,6):
    num = int(input(f'Digite {i}º número: '))
    conj.add(num)

print(f'O conjunto possui {len(conj)} elementos!')
'''