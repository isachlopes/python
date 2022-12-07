'''
public, protected, private
'''
class BaseDeDados:
    def __init__(self):#construtor do python
        self._dados = {}
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})
    
    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'rose')
bd.inserir_cliente(2, 'mario')
bd.inserir_cliente(3, 'raul')
bd.lista_clientes()
print(bd._dados)