#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ele
n = input('Digite algo: ')
print('É numérico:', n.isnumeric())
print('O tipo primitivo é:',type(n))
print('Só tem espaços?:', n.isspace())
print('É alfabetico?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada', n.istitle())

