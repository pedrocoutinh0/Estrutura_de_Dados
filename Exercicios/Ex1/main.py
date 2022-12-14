# Queremos usar listas encadeadas para implementar operacoes de conjuntos. Apresente uma solucao (codigo)
# que contempla as seguintes operacoes.
# 1. Insercao um elemento x em um conjunto. Lembre que nao  ́e necessario inserir elementos repetidos no
# conjunto.

# 2. Uniao de dois conjuntos A e B, produzindo um novo conjunto como resultado e deixando A e B inalte-
# rados.

# 3. Intersecao de dois conjuntos A e B, produzindo um novo conjunto como resultado e deixando A e B
# inalterados.

from lista import Lista

listaA = Lista()
listaB = Lista()

listaA.adicionar_elemento(2)
listaA.adicionar_elemento(4)
listaA.adicionar_elemento(5)
listaA.adicionar_elemento(9)
listaA.adicionar_elemento(4)

listaB.adicionar_elemento(2)
listaB.adicionar_elemento(5)
listaB.adicionar_elemento(3)
listaB.adicionar_elemento(1)
listaB.adicionar_elemento(2)

print(listaA)
print(listaB)

uniao = listaA.uniao(listaB)

print(uniao)

intersec = listaA.interseccao(listaB)

print(intersec)