n1 = float(input('Valor de N1: '))
n2 = float(input('Valor de N2: '))

m = (n1 + n2) / 2

print('Média: {:.1f}'.format(m))

# print('Parabéns' if m >= 6 else 'Estude mais!')

if m >= 6.0:
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado!')
