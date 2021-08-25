#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes
print('*-'*20)
print('Analisador de triângulos')
print('*-'*20)
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
if a < b + c and b < a + c and c < a + b:
    if a != b and a != c and b != c:
        print('Os Seguimentos podem formar um trângulo escaleno.')
    elif a == b == c:
        print('Os seguimentos acima podem formar um triângulo equilátero.')
    else:
        print('Os seguimento acima podem formar um triangulo isósceles')
else:
    print('Os segumento não podem formar um triângulo')