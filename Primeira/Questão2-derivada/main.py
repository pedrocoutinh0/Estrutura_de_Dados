from poli import Poli

poli1 = Poli()
poli2 = Poli()

poli1.inserir_termo(2, 0)
poli1.inserir_termo(5, 3)
poli1.inserir_termo(2, 5)

poli2.inserir_termo(1, 0)
poli2.inserir_termo(3, 3)

soma = poli1.somar(poli2)

valor = poli1.calcular(2)

deriv1 = poli1.derivada()
deriv2 = poli2.derivada()

print("")
