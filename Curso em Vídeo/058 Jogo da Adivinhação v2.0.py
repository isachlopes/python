#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
pc = randint(0, 10)
cont = 0
print('Tente adivinhar...\nPensei em um número entre 0 e 10 consegue adivinhar?')
certo = False
while not certo:
    jogador = int(input('Tente adivinhar: '))
    cont += 1
    if jogador == pc:
        certo = True
    else:
        if jogador > pc:
            print('Menos... Tente outra vez.')
        elif jogador < pc:
            print('Mais... Tente novamente!')
print(f'Acertou com {cont} palpites. Parabéns!')
print('fim')