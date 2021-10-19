#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
from urllib import request

try:
    site = request.urlopen('https://ibdrones.com.br/')
except:
    print('Deu erro')
else:
    print('Tudo ok')
    print(site.read())
