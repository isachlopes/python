#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado!')
    else:
        print('Número repetido!')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar[S/N]? ')).upper().strip()[0]
    if continua == 'N':
        break
lista.sort()
print(f'Os valores adicionados foram {lista}.')