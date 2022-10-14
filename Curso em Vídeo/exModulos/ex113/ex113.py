#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from leia import leiafloat, leiaint
    
n1 = leiaint('Digite um número: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n1} e o número Real {n2}.')