#programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
mai = 0
men = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if c==0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print(f' Você digitou os valores {valores}.')
print(f'o menor valor foi {men} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
print(f'O maior valor foi {mai} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()