#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(frase):
    print('~' * (len(frase) + 4))
    print(f'  {frase}')
    print('~' * (len(frase) + 4))
    print()

escreva('Vai toma o cu')
escreva('vagabundo')
