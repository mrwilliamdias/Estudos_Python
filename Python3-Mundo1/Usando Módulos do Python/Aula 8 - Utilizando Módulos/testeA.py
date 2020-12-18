import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
potencia = math.pow(num, num)
print('Raiz do Número: {}\n'
      'Potência do Número no Mesmo Número: {}\n'
      .format(math.floor(raiz), math.ceil(potencia)))
