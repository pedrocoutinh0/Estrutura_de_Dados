class No:
#construtor
    def __init__(self, dado):
        self.esq = None
        self.dir = None
        self.dado = dado
# transforma  ́arvore em string (somente para impressao)
    def __repr__(arv):
        return ("[" + str(arv.dado) + ", " + str(arv.esq) + ", " + str(arv.dir) +"]")

# conta o n ́umero de elementos armazenados
    def num_elemen(self):
        n = 1
        if self.esq is not None:
            n = n + self.esq.num_elemen()
        if self.dir is not None:
            n = n + self.dir.num_elemen()
        return n