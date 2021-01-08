num = int(input('Digite um número: '))

print('\nNúmero Digitado: {}'.format(num))

mod = num % 2

if mod == 0:
    print('Esse número é PAR!')
else:
    print('Esse número é IMPAR!')