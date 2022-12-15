from classes import Cliente, Endereco


cl1 = Cliente('Luiz', 32)
cl1.insere_endereco('Pelotas', 'RS')
cl2 = Cliente('Luiza', 39)
cl2.insere_endereco('Jurara', 'RJ')
cl2.insere_endereco('URURU', 'RN')

print(cl1.nome)
cl1.lista_enderecos()

cl2.lista_enderecos()