#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Seu nome completo em Maiusculas é {nome.upper()}.')
print(f'Seu nome completo em minusculas é {nome.lower()}.')
print('O seu nome tem no total {} letras.'.format(len(nome)- nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))