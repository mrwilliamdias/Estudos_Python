real = float(input('Digite o Valor da Carteira em Real: R$ '))
dolar = float(input('Digite a Cotação do Dolar no Dia Atual: U$ '))
compra = real / dolar
print('Valor da Carteira: R$ {:.2f}\n'
      'Cotação do Dolar por Real: R$ {:.2f}\n'
      'Valor Compra Dolar: U$ {:.2f}\n'.format(real, dolar, compra))
