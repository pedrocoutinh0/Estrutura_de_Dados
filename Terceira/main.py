# Participantes da Equipe:
# Pedro Lucas Coutinho de Araújo 
# Cristiano Henrique Bonfim Frota
from arvore import ArvBinariaBusca

arvore = ArvBinariaBusca(8)

arvore.inserir(5)
arvore.inserir(7)
arvore.inserir(4)
arvore.inserir(1)
arvore.inserir(20)
arvore.inserir(11)
arvore.inserir(12)
arvore.inserir(9)

print(arvore)

print("Ordem Crescente")
arvore.em_ordem_cres()
print("Ordem Decrescente")
arvore.em_ordem_decres()
print("Ordem de Nivel")
arvore.em_ordem_nivel()