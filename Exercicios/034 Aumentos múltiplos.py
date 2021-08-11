#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Qual o valor do salário do funcionário: '))
if sal > 1250:
    bonus = sal * 1.10
else:
    bonus = sal * 1.15
print(f'Quem ganhava R${sal:.2f} passa a ganhar R${bonus:.2f}.')