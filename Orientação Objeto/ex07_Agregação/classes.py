#Agregação está dentro da associação, onde está classe usa a outra como parte de si e precisando obrigatoriamente desta
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = [] #sempre qie eu incluir produtos vai ser uma classe inteira de produtos que vai ser incluida
        
    def inserir_produto(self, produto):#aqui vamos inserir os produtos
        self.produtos.append(produto)
    
    def lista_produto(self): #exibir os produtos
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    
    def soma_total(self):# somatorio total
        total = 0
        for produto in self.produtos:
            total += produto.valor
            return total
        

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor