'''Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
Em seguida, verifique se o nome 'Maria' está presente na tupla.'''

nome1 = input('Digite o 1º nome: ')
nome2 = input('Digite o 2º nome: ')
nome3 = input('Digite o 3º nome: ')

tup = (nome1, nome2, nome3)

if 'Maria' in tup or 'maria' in tup:
    print('Nome Maria presente na tupla!')
else: 
    print('Nome Maria não está presente na tupla!')
    
