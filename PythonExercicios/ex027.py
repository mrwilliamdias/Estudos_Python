name = str(input('Digite o nome completo: ')).strip()

slip_name = name.split()

print('Primeiro Nome: {}'.format(slip_name[0]))
print('Último Nome: {}'.format(slip_name[len(slip_name) - 1]))
