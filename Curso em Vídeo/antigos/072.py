#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""
e = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

while True:
    n = int(input('Digite um número de 0 a 5: '))
    if 0<= n <= 5:
        break
print(f'Você digitou o número {e[n]}')