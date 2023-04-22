'''Crie um dicionário vazio. Peça para o usuário digitar as chaves e os valores desse dicionário. Em seguida, adicione
uma nova chave e valor ao dicionário, onde a chave é 'cidade' e o valor é a cidade em que o usuário nasceu.'''

dic = {}

for i in range(1,4):
    chave = input('Digite uma chave: ')
    valor = input('Informe um valor: ')
    dic[chave] = valor

cidade = input('Digite a cidade em que nasceu: ')
dic['cidade'] = cidade

print(dic)

#é possivel fazer usando a funcao do python dic.update({'cidade' = cidade})