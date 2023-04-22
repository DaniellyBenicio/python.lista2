'''
Crie um dicionário vazio. Peça para o usuário digitar uma chave e um valor e adicione esses dados ao dicionário. 
Em seguida,peça para o usuário adicionar mais uma chave e um valor e adicione esses dados ao dicionário também
'''

dic = {}
#podia ser dict()

chave = input('Digite uma chave: ')
valor = input('Informe um valor: ')
dic[chave] = valor

chave2 = input('Digite uma segunda chave: ')
valor2 = input('Informe um segundo valor: ')
dic[chave2] = valor2

print(dic)