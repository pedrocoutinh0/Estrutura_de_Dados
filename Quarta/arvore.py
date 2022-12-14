class ArvBinariaBusca:

    # construtor
    def __init__(self, dado=None, pai = None):
        self.esq = None
        self.dir = None
        self.dado = dado
        self.pai = pai

    # transforma árvore em string (somente para impressao)
    def __repr__(arv):
        return ("[" + str(arv.dado) + ",  " + str(arv.esq) + ", " + str(arv.dir) +
                "]")

    # insere um novo item na árvore
    def inserir(raiz, dado):
        if not raiz.dado:
            raiz.dado = dado
        else:
            # não permite elementos repetidos
            if raiz.dado == dado:
                return
            # para que lado ir ?
            elif raiz.dado < dado:
                # se existe sub-árvore à direita
                if raiz.dir:
                    raiz.dir.inserir(dado)
                else:
                    raiz.dir = ArvBinariaBusca(dado, raiz)
            else:
                # se existe sub-árvore à esq
                if raiz.esq:
                    raiz.esq.inserir(dado)
                else:
                    raiz.esq = ArvBinariaBusca(dado, raiz)
        return

    def busca(raiz, dado):
        if raiz is None or raiz.dado == dado:
            return raiz
        else:
            if raiz.dado < dado:
                return raiz.dir.busca(dado)
            else:
                return raiz.esq.busca(dado)

    def altura(raiz):
        alturadir = 1
        alturaesq = 1
        if not (raiz.dir or raiz.esq):
            return 0
        if raiz.esq != None:
            alturaesq += raiz.esq.altura()
        if raiz.dir != None:
            alturadir += raiz.dir.altura()
        if alturaesq > alturadir:
            return alturaesq
        else:
            return alturadir













