valor = float(input('Bem vindo ao Descontrometro\n'
                    '===========================\n'
                    'Por favor, digite o valor do produto: R$ '))
desconto = float(5)
valorDoDesconto = (desconto*valor)/100
valorFinal = valor - valorDoDesconto
print('===========================\n'
      'Valor do Produto: R$ {:.2f}\n'
      'Porcentagem padrão de desconto: {:.0f}%\n'
      '===========================\n'
      'Valor Descontado: R$ {:.2f}\n'
      'Valor Final do Produto com Desconto: R$ {:.2f}'.format(valor, desconto, valorDoDesconto, valorFinal))
