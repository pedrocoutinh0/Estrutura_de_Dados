class No:
#construtor
    def __init__(self, dado):
        self.esq = None
        self.dir = None
        self.dado = dado

# transforma  ́arvore em string (somente para impressao)
    def __repr__(arv):
        return ("[" + str(arv.dado) + ", " + str(arv.esq) + ", " + str(arv.dir) +"]")

# Como saber o numero de nos armazenados em uma arvore? Apresente uma solucao recur-
# siva.
    def num_elemen(self):   
        n = 1
        if self.esq is not None:
            n = n + self.esq.num_elemen()
        if self.dir is not None:
            n = n + self.dir.num_elemen()
        return n
#Apresente um metodo recursivo para encontrar o maior elemento armazenado em uma
#arvore.
    def maiorfunc(self, maior):

        if self.dado >= maior:
            maior = self.dado
        
        if self.esq:
            maior = self.esq.maiorfunc(maior)
        if self.dir:
            maior = self.dir.maiorfunc(maior)

        return maior
# Uma  ́arvore bin ́aria  ́e dita completa se todos os seus n ́os possuem 2 filhos ou nenhum filho.
# Escreva c ́odigo para verificar se uma  ́arvore  ́e completa, tendo como entrada a raiz dessa
#  ́arvore.
    def verificar_arvore_completa(self):
        if not (self.esq and self.dir):
           return True 
        if not (self.esq.verificar_arvore_completa() and self.dir.verificar_arvore_completa()):
            return True
        else:
            return False
        
        