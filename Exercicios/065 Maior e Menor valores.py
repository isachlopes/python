#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = cont = 0
saida = 'S'
while saida == 'N':
    if saida == 'S':
        n = int(input('Digite um número: '))
        soma += n
        cont += 1
        saida = str(input('Quer continuar [S/N]?: ')).upper()

print(f'Você digitou {cont} números e a média foi {soma / cont}')