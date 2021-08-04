#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
conta = frase.count('A')
prime = frase.find('A')
print(f'A letra a aparece {conta} vezes na frase.')
#print(f'A letra a aparece a primeira vez na posição {}.')
#print(f'A letra A aparecea ultima vez na possição {}.')