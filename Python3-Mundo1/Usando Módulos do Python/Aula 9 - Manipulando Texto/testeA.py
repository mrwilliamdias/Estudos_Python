print("""
Python é uma linguagem de programação de alto nível, interpretada, de script, 
imperativa,orientada a objetos, funcional, de tipagem dinâmica e forte. 
Foi lançada por Guido van Rossum em 1991
""")

frase = '   Curso em Vídeo Python   '

print('Selecionando o a partir do 9º espaço e pulando 2 casas: ', frase[9::2])
print('Transformando todas em maiúsculo e contado todos os E maiúsculos: ', frase.upper().count('E'))
print('Contando a frase crua: ', len(frase))
print('Contando a frase  excluindo os espaços desnecessários: ', len(frase.strip()))
print('Trocando palavras apenas na exibição: ', frase.replace('Python', 'Android'))
print('Frase ainda crua: ', frase)

#Aqui modificamos a frase realmente:
frase = frase.replace('Python', 'Android')
print('Frase após modificações: ', frase)

divida = frase.split()
print('Está é a frase quebrada: ', divida)
print('E assim é possível selecionar a parte quebrada da frase: ', divida[3])
