sal = float(input('Salário do Funcionario: '))

if sal > 1250:
    per = int(10)
    valor = (sal / 100) * per
    total = sal + valor
else:
    per = int(15)
    valor = (sal / 100) * per
    total = sal + valor

print('\nSalário Atual: R$ {:.2f}\n'
      'Percentual de Aumento: {}%\n'
      'Diferença no Salário: R$ {:.2f}\n'
      'Salário Final: R$ {:.2f}\n'
      .format(sal, per, valor, total))
