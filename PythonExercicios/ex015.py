print('Sistema de Calculo de Aluguel de Carro\n'
      '======================================\n')
km = float(input('Digite a quantidade de Km percorrido: '))
dias = int(input('Digite a quantidade de dias alugados: '))
valorKm = km * 0.15
valorDias = dias * 60
final = valorDias + valorKm
print('======================================\n'
      'Km percorridos =  {:.2f}km\n'
      'Valor por km = R$ {:.2f}\n'
      'Valor total km = R$ {:.2f}\n'
      '______________________________________\n'
      'Dias alugados =  {} dias\n'
      'Valor por dia = R$ {:.2f}\n'
      'Valor total dias = R$ {:.2f}\n'
      '______________________________________\n'
      'Valor Total Aluguel do Carro: R$ {:.2f}'.format(km, 0.15, valorKm, dias, 60, valorDias, final))
