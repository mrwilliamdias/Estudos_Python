c = float(input('Sistema de Conversão de Celsius em Fahrenheit\n'
                '=============================================\n'
                'Digite o valor em Celsius: '))
f = (9 / 5 * c) + 32
print('=============================================\n'
      'Graus em Celsius: {:.1f}ºC\n'
      'Graus em Fahrenheit: {:.1f}ºF'.format(c, f))
