'''Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
Em seguida, verifique se o número 3 está presente no conjunto.'''

conj = set()

for i in range(1,6):
    num = int(input(f'Informe {i}º número: '))
    conj.add(num)

if 3 in conj:
    print('O número está presente no conjunto!')
else:
    print('Número não está presente no conjunto: ', conj)
