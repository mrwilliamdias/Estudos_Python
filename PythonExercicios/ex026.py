phrase = str(input('Digite uma frase: ')).strip()

lower_phrase = phrase.lower()

print('Quantas vezes a letra "A" aparece na frase: {}'.format(lower_phrase.count('a')))
print('A primeira letra "A" aparece na: {}ª Posição'.format(lower_phrase.find('a')+1))
print('A última letra "A" aparece na: {}ª Posição'.format(lower_phrase.rfind('a')+1))
