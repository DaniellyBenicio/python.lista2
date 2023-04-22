'''Peça para o usuário digitar 10 números e crie um conjunto com esses números. 
Em seguida, remova todos os números pares do conjunto.'''

conj = set()

for i in range(1,11):
    num = int(input(f'Informe {i}º número: '))
    conj.add(num)

conj = conj.copy() 

for num in conj.copy():
    if num % 2 == 0:
        conj.remove(num)

print(conj)
