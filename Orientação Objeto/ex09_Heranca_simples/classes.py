#é onde um objeto é outro objeto

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



class Cliente(Pessoa):# vao herdar tudo que tem em pessoa
    pass
#podemos criar metodos especificos tambem
class Aluno(Pessoa):
    pass