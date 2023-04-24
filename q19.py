'''Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
Em seguida, verifique quantos elementos estão no conjunto.'''


conj = set()

for i in range(1,6):
    num = int(input(f'Digite {i}º número: '))
    conj.add(num)

print(f'O conjunto possui {len(conj)} elementos!')

