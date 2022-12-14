
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
        self.max = None

    def __repr__(self):

        return str(self.inicio)

    def adicionar_elemento(lista, novo_dado):

        if lista.max != None and lista.max < novo_dado:

            lista.max = novo_dado
        elif lista.max == None:
            lista.max = novo_dado

        novo_no = No(novo_dado)

        novo_no.prox = lista.inicio

        lista.inicio = novo_no

    def busca(lista, valor):

        atual = lista.inicio

        while atual and atual.dado != valor:

            atual = atual.prox

        return atual

    def busca_max(lista):

        return lista.max

    def remove(lista, valor):
        assert lista.inicio, "Impossível remover valor de lista vazia."

        if lista.inicio.dado == valor:
            if valor == lista.max:
                atual = lista.inicio.prox
                maior = atual.dado
                while atual and atual.dado != None:
                    if atual.dado > maior:
                        maior = atual.dado
                    atual = atual.prox
                lista.max = maior
            lista.inicio = lista.inicio.prox

        else:
            anterior = None
            corrente = lista.inicio
            atual = lista.inicio
            maior = atual.dado
            while atual and atual.dado != None:
                if valor == lista.max and atual.dado != lista.max:
                    if atual.dado > maior:
                        maior = atual.dado
                if corrente.dado != valor:
                    anterior = corrente
                    corrente = corrente.prox
                atual = atual.prox
            if valor == lista.max:
                lista.max = maior
            if corrente:
                anterior.prox = corrente.prox
            else:
                anterior.prox = None






