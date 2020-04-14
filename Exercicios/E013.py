#faça um algoritmo que leia o salario de um funcionario e mostre o seu novo salario com 15%de aumento.
a = float(input('Quanto o funcionário ganha?: R$'))
#b = a*1.15
b = a + (a*15/100)#pode ser assim tambem
print('Após um aumento de 15%, o novo salário do funcionário é de R${:.2f}.'.format(b))
