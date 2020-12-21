from random import choice
# from random import randint

print('Sistema de Sorteios de Alunos\n'
      '=====================================================')
# num = randint(1, 4)
#
# if num == 1:
#     print('William, você foi o sorteado para limpar o quadro. ')
#
# elif num == 2:
#     print('Grasiele, você foi o sorteado para limpar o quadro. ')
#
# elif num == 3:
#     print('Daniel, você foi o sorteado para limpar o quadro. ')
#
# elif num == 4:
#     print('Leonardo, você foi o sorteado para limpar o quadro. ')

a1 = str(input('Escreva o nome do primeiro aluno: '))
a2 = str(input('Escreva o nome do segundo aluno: '))
a3 = str(input('Escreva o nome do terceiro aluno: '))
a4 = str(input('Escreva o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno que vai limpar o quadro é o {}'.format(escolhido))
