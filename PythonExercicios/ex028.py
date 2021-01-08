from random import randint
from time import sleep

random_num = randint(0, 5)

user_num = int(input('Bem vindo ao Jogo da Adivinhação!\n'
                     'Tente adivinhar qual é o número que o computador está pensando.\n'
                     '\n'
                     'Digite um número entre 0 à 5: '))

print('Seu número é: {}'.format(user_num))

print('Processando...')
sleep(3)

if user_num == random_num:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou!')

print('Número do Computador: {}'.format(random_num))
