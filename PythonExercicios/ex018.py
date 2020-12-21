from math import tan, cos, sin, radians
print('Sistema de Calculo de Seno, Cosseno e Tangente')
ang = int(input('Digite o Ângulo: '))
print('==============================================\n'
      'Ângulo: {}º\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}\n'
      .format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
