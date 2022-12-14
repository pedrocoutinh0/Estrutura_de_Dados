#Parcipantes: Pedro Lucas Coutinho de Araújo e Cristiano Henrique Bonfim Frota
from arvore import ArvBinariaBusca
from arvoresembusca import No

def verificararvore(raiz):
    dir = True
    esq = True
    if raiz.dir != None:
        if raiz.dir.dado > raiz.dado:
            dir = verificararvore(raiz.dir)
        else:
            dir = False
    if raiz.esq != None:
        if raiz.esq.dado < raiz.dado:
            esq = verificararvore(raiz.esq)
        else:
            esq = False
    return dir and esq


raiz = ArvBinariaBusca()
raizno = No(10)

raiz.inserir(10)
raiz.inserir(5)
raiz.inserir(17)
raiz.inserir(4)
raiz.inserir(14)
raiz.inserir(25)
raiz.inserir(1)
raiz.inserir(2)

raizno.dir = No(17)
raizno.dir.dir = No(25)
raizno.dir.esq = No(14)
raizno.esq = No(5)
raizno.esq.dir = No(4)
raizno.esq.esq = No(1)
raizno.esq.esq.dir = No(2)

print(raiz)

print(raiz.altura())

print(verificararvore(raiz))

print(verificararvore(raizno))
