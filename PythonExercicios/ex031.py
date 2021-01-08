distance = float(input('Distância percorrida em Km: '))

print('\nR$ 0,50 por Km até 200Km no total.\n'
      'R$ 0,45 por Km para viagens além acima de 200Km.')
print('\nDistância da viagem: {:.1f}Km'.format(distance))

# ticket = distance * 0.5 if distance <= 200 else distance * 0.45

if distance > 200:
    ticket = distance * 0.45

else:
    ticket = distance * 0.5

print('\nValor da passagem: R$ {:.2f}'.format(ticket))


