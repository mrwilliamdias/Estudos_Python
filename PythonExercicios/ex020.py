from random import shuffle
print('Sistem de Sorteio de Ordem de Apresentação\n'
      '==========================================')
a1 = str(input('Digite o Nome do Primeiro Aluno: '))
a2 = str(input('Digite o Nome do Segundo Aluno: '))
a3 = str(input('Digite o Nome do Terceiro Aluno: '))
a4 = str(input('Digite o Nome do Quarto Aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('=========================================\n'
      '1º: {}\n'
      '2º: {}\n'
      '3º: {}\n'
      '4º: {}\n'
      .format(lista[0], lista[1], lista[2], lista[3]))
