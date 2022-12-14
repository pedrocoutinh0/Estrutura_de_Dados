from fila import Fila

class ArvBinariaBusca :
# construtor
    def __init__ (self, dado = None):
        self.esq = None
        self.dir = None
        self.dado = dado
# transforma rvore em string ( somente para impressao )
    def __repr__ (arv):
        return ("[" + str (arv.dado) + ", " + str (arv.esq) + ", " + str (arv.dir) +"]")

# insere um novo item na rvore
    def inserir(raiz, dado):
        if not raiz.dado :
            raiz.dado = dado
        else :
# nao permite elementos repetidos
            if raiz.dado == dado :
                return
# para que lado ir ?
            elif raiz.dado < dado :
# se existe sub - arvore a direita
                if raiz.dir:
                    raiz.dir.inserir(dado)
                else :
                    raiz.dir = ArvBinariaBusca(dado)
            else :
# se existe sub - arvore a esq
                if raiz.esq:
                    raiz.esq.inserir(dado)
                else :
                    raiz.esq = ArvBinariaBusca(dado)
        return
# Percurso Em Ordem
    def em_ordem_cres(raiz):
# visita sub - arvore esquerda
        if raiz.esq :
            raiz.esq.em_ordem_cres()
# visita raiz
        print(raiz.dado)
# visita sub - arvore direita
        if raiz.dir :
            raiz.dir.em_ordem_cres()

    def em_ordem_decres(raiz):
        
        if raiz.dir :                  # Primeiro entrará numa recursividade em que buscará o maior valor da arvore imprimindo-o na tela,  
            raiz.dir.em_ordem_decres() # após isso irá printar o segundo maior que pode estar na sua esquerda ou ser seu pai. Dessa forma,
                                       # a lógica segue para os outro níveis da árvore
        print(raiz.dado)
        
        if raiz.esq :
            raiz.esq.em_ordem_decres()
    
    def em_ordem_nivel(raiz):

        f = Fila()
        f.enfileirar(raiz)
        x = raiz
        while f.inicio:
            
            if x:
                x = f.desenfileirar()
                print(x.dado)
            
            if x.esq :
                f.enfileirar(x.esq)
           
            if x.dir :
                f.enfileirar(x.dir)



        

        