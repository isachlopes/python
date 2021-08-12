#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('*-'*20)
print('Analisador de triângulos')
print('*-'*20)
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos podem formar um triângulo.')
else:
    print('Os segumento não podem formar um triângulo')