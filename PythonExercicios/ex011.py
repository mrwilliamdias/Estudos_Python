altura = float(input('Digite o valor da ALTURA da parede em METROS: '))
largura = float(input('Digite o valor da LARGURA da parede em METROS: '))
area = largura * altura
tinta = float(2)
print('Altura da Parede: {:.2f}m\n'
      'Largura da Parede: {:.2f}m\n'
      'Área da Parede: {:.2f}m²\n'
      'Tinta Pinta: {:.2f}m²/l\n'
      'Qtd. Tinta Necessária: {:.2f}l'.format(altura, largura, area, tinta, area / tinta))
