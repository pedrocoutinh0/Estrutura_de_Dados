class No:

    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.prox = proximo

    def __repr__(self):
        if self.prox == None:
            return '%s' % (self.dado)
        return '%s %s' % (self.dado, self.prox)

class Lista:

    def __init__(self):
        self.inicio = None

    def __repr__(self):

        return str(self.inicio)

    def adicionar_elemento(lista, novo_dado):

        teste = lista.inicio

        while teste and teste.dado != None:
            if teste.dado == novo_dado:
                return
            teste = teste.prox

        novo_no = No(novo_dado)

        novo_no.prox = lista.inicio

        lista.inicio = novo_no

    def busca(lista, valor):

        atual = lista.inicio

        while atual and atual.dado != valor:

            atual = atual.prox

        return atual

    def interseccao(lista, listaA):
        intersec = Lista()
        lista1 = lista.inicio
        lista2 = listaA.inicio

        while lista1 and lista1.dado != None:
            while lista2 and lista2.dado != None:
                if lista1.dado == lista2.dado:
                    intersec.adicionar_elemento(lista1.dado)
                lista2 = lista2.prox
            lista2 = listaA.inicio
            lista1 = lista1.prox

        return intersec
    def uniao(lista, listaA):
        uni = Lista()
        lista1 = lista.inicio
        lista2 = listaA.inicio
        while lista1 and lista1.dado != None:
            uni.adicionar_elemento(lista1.dado)
            lista1 = lista1.prox
        while lista2 and lista2.dado != None:
            uni.adicionar_elemento(lista2.dado)
            lista2 = lista2.prox

        return uni







