sal = float(input('Bem Vindo ao Sistema de Aumento Salarial\n'
                  '========================================\n'
                  'Por favor, digite o valor do salário: R$ '))
aum = int(15)
dif = sal * (aum / 100)
final = sal + dif
print('========================================\n'
      'Valor Atual do Salário: R$ {:.2f}\n'
      'Porcentagem de Aumento: {}%\n'
      '========================================\n'
      'Aumento de: R$ {:.2f}\n'
      'Salário Final Com Aumento: R$ {:.2f}'.format(sal, aum, dif, final))

