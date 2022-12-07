class Teste:
    atual = 2022
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def nasc(self):
        print(self.atual - self.idade)
        
    def nasc2(self):
        self.atual = 2029
        print(self.atual - self.idade)
        

p1 = Teste('gomes', 45)

p1.nasc()
p1.nasc2()