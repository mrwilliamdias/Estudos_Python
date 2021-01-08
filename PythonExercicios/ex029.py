car_speed = int(input('Velocidade do carro: '))

print('Velocidade máxima da rodovia: 80km/h\n'
      'Sua velocidade: {}km/h'.format(car_speed))

if car_speed > 80:
    traffic_ticket = (car_speed - 80) * 7
    print('Você foi multado!\n'
          'Valor da multa: R$ {:.2f}'.format(traffic_ticket))
