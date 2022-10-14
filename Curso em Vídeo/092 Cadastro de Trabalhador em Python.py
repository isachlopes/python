#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
work  = dict()
work['nome'] = str(input('Nome: ')).capitalize()
nascimento = int(input('Ano de nascimento: '))
work['idade'] = date.today().year - nascimento
carteira = int(input('Carteira de trabalho:[0 não tem] '))
if carteira != 0:
    work['CTPS'] = carteira
    work['contratação'] = int(input('Ano de contratação: '))
    work['salario'] = float(input('Salário: R$'))
    work['aposentadoria'] = (work['contratação'] - nascimento) + 30
print('-=' * 20)
for k, v in work.items():
    print(f'- {k} tem valor {v}.')
