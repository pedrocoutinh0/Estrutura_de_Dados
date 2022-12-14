class No:
    """Esta classe representa um item em uma pilha."""

    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.prox = proximo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.prox)


class Pilha:
    """Esta classe implementa uma pilha."""

    def __init__(pilha):
        pilha.topo = None

    def __repr__(pilha):
        return '[%s]' % (pilha.topo)

    def vazia(pilha):
        return pilha.topo == None

    def obter_topo(pilha):
        return pilha.topo.dado

    def empilhar(pilha, novo_dado):
        novo_no = No(novo_dado, pilha.topo)
        pilha.topo = novo_no

    def desempilhar(pilha):
        if pilha.vazia():
            print('erro: a pilha vazia')
            return None

        t = pilha.topo
        pilha.topo = pilha.topo.prox
        return t.dado