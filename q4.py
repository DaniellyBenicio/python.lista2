'''
Peça para o usuário digitar 5 números e crie um conjunto com esses números. 
Em seguida, peça para o usuário escolher um dos números e removê-lo do conjunto.
'''

conj = set()

for i in range(1,6):
    num = int(input(f'Digite {i}º número: '))
    conj.add(num)

print(conj)

escolha = int(input('\nEntre os números informados, escolha um para ser removido do conjunto: '))

if escolha in conj:
    conj.remove(escolha)
    print('Número removido com sucesso!')
    print(conj)
else:
    print('Número não encontrado no conjunto!')
    


#conj.discard(escolha) CASO ESCOLHESSE ESSE METODO, NAO REMOVERIA O NUMERO, APENAS SE O USUARIO INFORMASSE UM NUMERO
#QUE NAO ESTIVESSE NO CONJUNTO, ELE REPETIRIA O CONJUNTO.
