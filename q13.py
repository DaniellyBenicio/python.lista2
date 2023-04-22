'''Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. 
Em seguida, verifique se a chave 'profissão' está presente no dicionário.'''

dic = {}

for i in range(1,4):
    chave = input('Informe a chave: ')
    valor = input('Informe o valor: ')
    dic[chave] = valor

if 'profissao' in dic.keys():
    print("A chave 'profissao' está presente no dicionário")
else:
    print('A chave não foi encontrada no dicionário!')