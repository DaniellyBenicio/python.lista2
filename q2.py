'''Peça para o usuário digitar 3 nomes e crie uma tupla com esses nomes. Em seguida, peça para o usuário 
ecolher um dos nomes e substituir esse nome por outro nome que ele também deve digitar'''

nomes = ()

for i in range(1,4):
    nome = input(f'Digite {i}º nome: ')
    nomes = nomes + (nome,) #a vírgula indicar que é uma tupla de um único elemento.
    
lista = list(nomes)

print('''Qual nome deseja substituir?
    1 - Primeiro
    2 - Segundo
    3 - Terceiro''')
escolha = int(input('Opção: '))

if escolha == 1:
    subs = input('Informe novo nome: ')
    lista[0] = subs
elif escolha == 2:
    subs = input('Informe novo nome: ')
    lista[1] = subs
elif escolha == 3:
    subs = input('Informe novo nome: ')
    lista[2] = subs
    
tuplaN = tuple(lista)

print(tuplaN)