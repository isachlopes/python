#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = cont = maior = menor = 0
resp = 'S'
while not resp == 'N':
    if resp == 'S':
        n = int(input('Digite um número: '))
        cont += 1
        soma += n
        resp = str(input('Quer continuar [S/N]?: ')).upper()
    if cont ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'Você digitou {cont} números e a média foi {soma / cont}')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')