from math import trunc
num = float(input('Digite um número Real: '))
print('{} é um Número Real, ele foi convertido em {} que é a sua forma de número Inteiro.'.format(num, trunc(num)))
print('{} é um Número Real, ele foi convertido em {} que é a sua forma de número Inteiro.'.format(num, int(num)))
print('{} é um Número Real, ele foi convertido em {:.0f} que é a sua forma de número Inteiro.'.format(num, num))
