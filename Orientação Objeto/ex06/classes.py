#Faz uma classe conversar com a outra, mas nenhuma 
#


class Escritor:
    def __init__(self, nome):#construtor
        self.__nome = nome #nome do escritor esta privado
       
        self.__ferramenta = None

    @property 
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')


