name = str(input('Digite o seu nome completo: ')).strip()

print('Nome: {}'.format(name))
print('Nome todo em minúsculo: {}'.format(name.lower()))
print('Nome todo em maiúsculo: {}'.format(name.upper()))

broken_name = name.replace(' ', '')

print('Nome sem espaços: {}'.format(broken_name))
print('Quantidade de caracteres com espaço: {}'.format(len(name)))
# print('Quantidade de caracteres sem espaço: {}'.format(len(name) - nome.count(' ')))
print('Quantidade de caracteres sem espaço: {}'.format(len(broken_name)))

split_name = name.split()

print('Nome quebrado: {}'.format(split_name))
# print('Quantidade de caracteres no primeiro nome: {}'.format(name.find(' ')))
print('Quantidade de caracteres no primeiro nome: {}'.format(len(split_name[0])))
