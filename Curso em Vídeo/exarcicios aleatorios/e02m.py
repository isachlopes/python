from e02 import Bombac as bc











print('Abastecendo seu carro')
fim  = False
while fim not in True:
    id = int(input('id do abastecimento: '))
    tipo_combustivel = input('qual o combustivel: ')
    valor_litro = input('valor_litro: ')
    quantidade_combustivel = input('quantidade_combustivel:')
    fim = input('fim?: ')
    if fim == True:
        v1 = bc(id, tipo_combustivel, valor_litro, quantidade_combustivel)
        break
    else:
        continue
                             
