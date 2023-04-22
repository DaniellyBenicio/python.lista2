'''Crie uma lista vazia e peça para o usuário digitar 10 números. 
Em seguida, adicione esses números à lista utilizando um loop for.'''

x = []

for i in range(1,11):
    num = int(input(f'Digite {i}° número: '))
    x.append(num)
print(x)