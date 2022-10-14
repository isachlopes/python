#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos você não vota.'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos o voto é facultativo.'
    elif 18 <= idade < 60:
        return f'Com {idade} anos o voto é obrigatório.'


nasceu = int(input('Ano de nascimento: '))
print(voto(nasceu))