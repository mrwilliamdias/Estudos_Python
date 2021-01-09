print('É possível formar um triângulo? \n')

r1 = float(input('Comprimento da Primeira Reta: '))
r2 = float(input('Comprimento da Segunda Reta: '))
r3 = float(input('Comprimento da Terceira Reta: '))

print('\nValor do Primeiro Segmento: {:.1f}\n'
      'Valor do Primeiro Segmento: {:.1f}\n'
      'Valor do Primeiro Segmento: {:.1f}\n\n'
      .format(r1, r2, r3))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('SIM, é possível formar um triângulo!')
else:
    print('NÃO é possível formar um triângulo!')
