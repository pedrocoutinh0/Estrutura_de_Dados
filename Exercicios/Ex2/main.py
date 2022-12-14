from arvore import No

def buscar(arvore, dado, no = No(0)):
    
    if arvore.dado == dado:
        return arvore
    
    if arvore.dir != None:
        if arvore.dir.dado != dado:
            no = buscar(arvore.dir, dado)
        else:
            no = arvore.dir
            return no

    if arvore.esq != None:
        if arvore.esq.dado != dado:
            no = buscar(arvore.esq, dado)
        else:
            no = arvore.esq
            return no 

    return no

def num_folha(arvore):
    n = 0
    if not (arvore.dir and arvore.esq):
        return 1
    if arvore.dir:
        n += num_folha(arvore.dir)
    if arvore.esq:
        n += num_folha(arvore.esq)
    return n

raiz = No(5)
raiz.esq = No(2)
raiz.dir = No(1)
raiz.dir.dir = No(7)
raiz.dir.esq = No(3)
raiz.esq.dir = No(6)
raiz.esq.esq = No(11)
raiz.dir.dir.dir = No(100)
raiz.dir.dir.esq = No(20)
raiz.dir.esq.dir = No(2)
raiz.dir.esq.esq = No(3)

print(raiz)

print(raiz.num_elemen())

print(raiz.maiorfunc(raiz.dado))

print(raiz.verificar_arvore_completa())

print(buscar(raiz, 2))

print(num_folha(raiz))