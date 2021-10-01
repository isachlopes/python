#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
def ajuda(whi):
    frase = '  Sistema de ajuda Pyhelp'
    print(f'{"~" * (len(frase) + 4)}\n{frase}\n{"~" * (len(frase) + 4)}')
    while True:
        return help(whi)
print(ajuda(input('Função ou biblioteca: ')))
