#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o sei nome completo: ')).capitalize().split()
print('Muito prazer em te conhecer: ')
print(f'Seu primeiro nome é {nome[0]}.\nSeu último nome é {nome[len(nome)-1]}.')