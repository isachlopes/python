#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
t1 = int(input('digite o primeiro termo: '))
r = int(input('Digita a razão da PA: '))
dec = t1 + (10-1) * r
for c in range(t1, dec + r, r):
    print(f'{c} ', end= ' ')
print('fim')


