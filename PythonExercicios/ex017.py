from math import hypot
print('HIPOTENUSA DE UM TRIÂNGULO RETÂNGULO')
catAd = float(input('Digite o valor do Cateto Adjascente: '))
catOp = float(input('Digite o valor do Cateto Oposto: '))
hip = hypot(catAd, catOp)
print('====================================\n'
      'Valor do Cateto Adjascente: {:.2f}\n'
      'Valor do Cateto Oposto: {:.2f}\n'
      '====================================\n'
      'Valor da Hipotenusa: {:.2f}\n'
      .format(catAd, catOp, hip))
