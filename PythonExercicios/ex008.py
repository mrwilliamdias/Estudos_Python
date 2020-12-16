m = float(input('Valor em Metros para a conversão: '))
cm = m * 100
mm = cm * 100
print('Convertendo...\n'
      '{:.1f} Metros\n'
      '{:.0f} Centímetros\n'
      '{:.0f} Milímetros\n'.format(m, cm, mm))
