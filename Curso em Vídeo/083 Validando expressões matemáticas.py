#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
abre = fecha = 0
exp = str(input('Digite uma expressão: '))
for l in exp:
    if '(' in l:
        abre += 1
    if ')' in l:
        fecha += 1
if abre == fecha:
    print('a expressão é válida')
else:
    print('A expressão não é válida')