'''Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
Em seguida, verifique se o nome 'Maria' está presente na tupla.'''

nome = []

for i in range(1,4):
    n = input(f'Informe o {i}º nome: ')
    nome.append(n)

tup = tuple(nome)

if 'Maria' in tup or 'maria' in tup or 'MARIA' in tup:
    print('O Nome "Maria" presente na tupla!')
else: 
    print('O nome "Maria" não está presente na tupla!')
    
