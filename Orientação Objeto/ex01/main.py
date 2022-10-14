from pessoa import Pessoa
from datetime import date
atual = date.today().year
p1 = Pessoa('Luiz', 45)
p2 = Pessoa('Lana', 22)
p1.comer('maça')
p1.falar('poo')
p1.parar_comer()
p1.falar('poo')
p1.comer('jaca')
p2.comer('Tatu')

print(atual)