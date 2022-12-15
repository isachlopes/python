from classes import Produto, CarrinhoDeCompras

carrinho = CarrinhoDeCompras() # pode existir sem os produtos
p1 = Produto('Camiseta', 50)
p2 = Produto('abacate', 5)
p3 = Produto('caneca', 55)

carrinho.inserir_produto(p1)# duplicar linha == shift +alt + setas
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())