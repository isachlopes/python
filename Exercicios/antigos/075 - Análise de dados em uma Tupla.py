#programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
a = (int(input('Digite o valor 1: ')),
     int(input('Digite o valor 2: ')),
     int(input('Digite o valor 3: ')),
     int(input('Digite o valor 4: ')))
print(f'Você digitou os valores: {a}')
print(f'O número 9 apareceu {a.count(9)} vezes.')
if 3 in a:
    print(f'O valor 3 apareceu na posição {a.index(3)+1}.')
else:
    print('O número 3 não se encontra.')
print('Os valores pares digitados foram: ', end='')
for n in a:
    if n % 2 == 0:
        print(n, end=' ')
