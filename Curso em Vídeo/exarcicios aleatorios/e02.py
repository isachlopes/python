"""  Classe Bomba de Combustível:
Classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel / valorLitro / quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) - método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) - método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) - altera o valor do litro do combustível.
alterarCombustivel( ) - altera o tipo do combustível.
alterarQuantidadeCombustivel( ) - altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba."""

registro = []

class Bombac:
    
    def __init__(self, id, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.id = id
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        atributos = {'id':self.id, 'tipo_combustivel': self.tipo_combustivel, 'valor_litro': self.valor_litro, 'quantidade_COMBUSTIVEL': self.quantidade_combustivel}
        registro.append(atributos)
        print(f'O abastercimento {self.id} colocou {self.quantidade_combustivel} litros de {self.tipo_combustivel} a R${self.valor_litro}')

        print(registro)
    def alterar_Combustivel(self, novo_combustivel):
        if atributos[novo_combustivel] != self.tipo_combustivel:
            registro['tipo_combustivel'] = novo_combustivel
        else:
            print('o cliente não mudou o combustivel')
        print(registro)


    def abastecer_por_valor(self, valor_litro,):
        pass

    def abastecer_por_litro(self):
        pass
    
    def alterar_valor(self):
        pass


    def alterar_qualtidade_de_bustivel(self):
        pass

