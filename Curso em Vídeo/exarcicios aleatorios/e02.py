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

class Bombac:
    registro= ['','','','']
    def __init__(self, id, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.id = id
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
        
    def alterar_Combustivel(self, novo_combustivel):
        if novo_combustivel != self.tipo_combustivel:
            novo_combustivel = self.tipo_combustivel
        else:
            print('o cliente não mudou o combustivel')
        
    def abastecer_por_valor(self, novo_valor_litro,):
        if novo_valor_litro != self.valor_litro:
            novo_valor_litro = self.valor_litro
        else:
            print('valor litro não mudou')

    def abastecer_por_litro(self):
        pass
    
    def alterar_valor(self):
        pass


    def alterar_qualtidade_de_bustivel(self):
        pass

