class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço
    
    def desconto(self, percentual):
        self.preço -= self.preço * (percentual / 100)
    #Getter
    @property #decorador
    def preço(self):
        return self._preço
    #Setter
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str): # vai verificar se o valor é um string
            valor = float(valor.replace('R$', '')) #vai transformar a string em um valor float
        self._preço = valor
        
        
p1 = Produto('Camiseta', 50)
p2 = Produto('calça', 'R$89')
p1.desconto(10)
print(p1.preço)

p2.desconto(10)
print(p2.preço)