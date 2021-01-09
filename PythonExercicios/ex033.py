print('Maior ou Menor? \n')

n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))
n3 = int(input('Digite o Terceiro Número: '))

print('\nPrimeiro Número: {}'
      '\nSegundo Número: {}'
      '\nTerceiro Número: {}\n'.format(n1, n2, n3))

if n1 > n2 and n1 > n3:
    print('Maior Número: {}'.format(n1))

if n2 > n1 and n2 > n3:
    print('Maior Número: {}'.format(n2))

if n3 > n1 and n3 > n2:
    print('Maior Número: {}'.format(n3))


if n1 < n2 and n1 < n3:
    print('Menor Número: {}'.format(n1))

if n2 < n1 and n2 < n3:
    print('Menor Número: {}'.format(n2))

if n3 < n1 and n3 < n2:
    print('Menor Número: {}'.format(n3))
