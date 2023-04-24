'''Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. 
Em seguida, verifique quantas vezes o nome 'Maria' aparece na tupla.'''

nome = []

for i in range(1,4):
    n = input(f'Informe o {i}º nome: ')
    nome.append(n)

tup = tuple(nome)
qnt = 0

for i in range(len(tup)):
    if tup[i].lower() == 'maria':
        qnt = qnt + 1
print(f'O nome Maria aparece {qnt} vezes!')

'''
for i in tup:
    if i.lower() == 'maria':
    qnt = qnt + 1
'''
