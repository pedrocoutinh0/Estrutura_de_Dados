class Poli_No :
    def __init__ ( self , coef = None , exp = None, proximo = None):

        self.coef = coef
        self.exp = exp
        self.prox = proximo

class Poli :

    def __init__ (self):
        self.inicio = None

    def inserir_termo (self, coef, exp):
        novo_termo = Poli_No()
        atual = self.inicio
        novo_termo.coef = coef
        novo_termo.exp = exp

        while atual and atual.coef != None:
            if novo_termo.exp == atual.exp:
                novo_termo.coef += atual.coef
                self.remove(exp)
            atual = atual.prox

        novo_termo.prox = self.inicio
        self.inicio = novo_termo

    def remove(self, exp):
        if self.inicio.exp == exp:
            self.inicio = self.inicio.prox
        else:
            anterior = None
            corrente = self.inicio
            while corrente and corrente.exp != exp:
                anterior = corrente
                corrente = corrente.prox
            if corrente:
                anterior.prox = corrente.prox
            else:
                anterior.prox = None

    def calcular (self, x ):
        poli = self.inicio
        valor = 0
        while poli and poli.coef != None:
            valor += poli.coef*(x**poli.exp)
            poli = poli.prox

        return valor

    def somar(self, poli):
       soma = Poli()
       atual = self.inicio
       atualpoli = poli.inicio


       while atualpoli and atualpoli.coef != None:
            soma.inserir_termo(atualpoli.coef, atualpoli.exp)
            atualpoli = atualpoli.prox

       while atual and atual.coef != None:
            soma.inserir_termo(atual.coef, atual.exp)
            atual = atual.prox

       return soma

    def derivada(self):
        deriv = Poli()
        atual = self.inicio

        while atual and atual.coef != None:
            if atual.exp != 0:
                coef = atual.coef * atual.exp
                exp = atual.exp - 1
                deriv.inserir_termo(coef, exp)
            atual = atual.prox

        return deriv



