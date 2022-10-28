class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando= False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo
        
    def comer(self, alimento):
        if self.comendo:
           print(f'{self.nome} já está comendo.')
           
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
        
        