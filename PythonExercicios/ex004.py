algo = input('Digite algo: ')
print('TIPO PRIMITIVO: ', type(algo))
print('"{}" somente tem espaços? '.format(algo), algo.isspace())
print('"{}" é um número? '.format(algo), algo.isnumeric())
print('"{}" é alfabético? '.format(algo), algo.isalpha())
print('"{}" é alfanumérico? '.format(algo), algo.isalnum())
print('"{}" está em maiúsculas? '.format(algo), algo.isupper())
print('"{}" está em minúsculas? '.format(algo), algo.islower())
print('"{}" está capitalizada? '.format(algo), algo.istitle())
