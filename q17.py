'''Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.'''

nome1 = input('Digite o 1º nome: ')
nome2 = input('Digite o 2º nome: ')
nome3 = input('Digite o 3º nome: ')

tup = (nome1, nome2, nome3)

qnt = tup.count('Maria')

if 'Maria' in tup:
    print(f'O nome Maria está presente na tupla! Aparece {qnt} vezes!')
else: 
    print('Nome não está presente na tupla!')