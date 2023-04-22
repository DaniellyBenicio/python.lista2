'''Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário.
Em seguida, retorne o valor da chave 'idade'.'''

dic = {}

for i in range(1,6):
    chave = input('Informe a chave: ')
    valor = input('Informe o valor: ')
    dic[chave] = valor

if 'idade' in dic:
    print('O valor da idade é: ', dic['idade'])
else:
    print('A chave idade não foi encontrada no dicionário!')