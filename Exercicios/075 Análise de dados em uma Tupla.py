#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
cont9 = 0
a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))
d = int(input('Digite o 4° número: '))
e = (a, b, c, d)
print(f'voce digitou os valores {e}')



print(f'O número 9 apareceu {e.count(9)} vezes.')
print(f'O número 3 apareceu a primeira vez na posição {e.index(3)}.')
print(f'Os valores pares digitados foram: ', end='')
for c in e:
    if c % 2 == 0:
        print(c, end=' ')