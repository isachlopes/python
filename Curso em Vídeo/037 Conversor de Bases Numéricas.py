#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 
# 2 para octal e 
# 3 para hexadecimal.
num = int(input('Digite um número: '))
print('Escolha um das bases de conversão: \n[ 1 ] converter para binário\n[ 2 ] converter para octal\n[ 3 ] converter para hexadecimal')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}.')
elif op == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif op == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida, tente novamente.')
print('Bom dia')
