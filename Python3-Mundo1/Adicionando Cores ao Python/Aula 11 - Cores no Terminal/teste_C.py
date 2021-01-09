nome = 'William'
cores = {'Limpa':'\033[m',
         'azul':'\033[34m'}

print('Olá, bem vindo {}{}{}!'.format(cores['azul'], nome, '\033[m'))
# print('Olá, bem vindo {}{}{}!'.format('\033[4;34m', nome, '\033[m'))