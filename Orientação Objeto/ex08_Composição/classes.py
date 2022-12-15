#é a relacamo mais forte entre classes. uma classe vai ser dona de objetos na outra classe

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado)) #chamar a classe aqui
        
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado