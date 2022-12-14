from lista import Lista

lista = Lista()

lista.adicionar_elemento(5)

lista.adicionar_elemento(7)

lista.adicionar_elemento(8)

lista.adicionar_elemento(4)

lista.adicionar_elemento(2)

print(lista)

print(lista.busca_max())

lista.adicionar_elemento(10)

print(lista.busca_max())

lista.remove(7)

print(lista)

print(lista.busca_max())

lista.remove(10)

print(lista)

print(lista.busca_max())

lista.remove(8)

print(lista)

print(lista.busca_max())