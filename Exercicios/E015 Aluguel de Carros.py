#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelo qual ele foi alugado. Calcule o total do preço a ser pago.
#Sabendo que o carro custa R$60,00/dia eR$15,00 /km rodado.
dias = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos quilômetros foram percorridos?: '))
custo = (dias*60)+(km*0.15)
print('Após {} dias de locação e {:.0f}km rodados, o custo total ficou em R${:.2f}.'.format(dias, km, custo))
