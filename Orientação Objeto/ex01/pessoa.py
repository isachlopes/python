class Pessoa:
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
        
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} já está falando sobre {assunto}.')
        self.falando = True
    
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False
    
    
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return        
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
        
        
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
        
        