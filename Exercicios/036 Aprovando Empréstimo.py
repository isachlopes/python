#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário: R$'))
anos = int(input('Quantos anos para pagar: '))
prestacao = casa / (anos* 12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}.')
if prestacao >= salario * 30/100:
    print('Empréstimo negado')
elif prestacao < salario * 30/100:
    print('Empréstimo autorizado.')