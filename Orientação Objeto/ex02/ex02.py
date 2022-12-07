from datetime import date
from random import randint


class Pessoa:
    from datetime import date
    ano_atual = date.today().year
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
        
    def ano_nascimento(self):
        print(self.ano_atual - self.idade)
        
    @classmethod
    def por_ano_nasc(cls, nome, nasc):
        idade = cls.ano_atual - nasc
        return cls(nome, idade)
    
    
    @staticmethod
    def usuario_id():
        rand = randint(10000, 99999)
        return rand
        
#p1 = Pessoa.por_ano_nasc('Ana', 1999)
p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.idade, p1.nome)
p1.por_ano_nasc()
print(Pessoa.usuario_id())
        
        