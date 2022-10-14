#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

peso = float(input('Qual o seu peso? (KG): '))
altura = float(input('Qual a sua altura?(m): '))
imc = peso / altura** 2
print(f'O IMC dessa pessoa é {imc:.1f}.')
if imc < 18.5:
    print('Peso abaixo do normal,')
elif 18.5 < imc <=24.9:
    print('Peso normal.')
elif 24.9 < imc <= 29.9:
    print('Sobrepeso.')
elif 29.9 < imc <= 34.9:
    print('Obesidade Grau I.')
elif 34.9 < imc <= 39.9:
    print('Obesidade grau II.')
elif imc > 39:
    print('Obesidade grau III ou mórbida. Cuidado!')
