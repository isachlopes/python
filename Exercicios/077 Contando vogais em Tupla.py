#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
p = ('cavalo', 'mamadeira', 'violino')
for c in p:
    print(f'\nPara a palavra {c.upper()} temos ', end='')
    for l in c:
        if l in 'aeiou':
            print(l.lower(), end= ' ')