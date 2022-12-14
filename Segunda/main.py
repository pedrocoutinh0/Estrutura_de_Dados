# Participantes da Equipe: Pedro Lucas Coutinho de Araújo e Cristiano Henrique Bonfim Frota
from passposfixa import *

infixa = "2*(3-5)+6/2"
posfixa = toposfixa(infixa)

print(posfixa)  # a saida esperada eh: 2 3 5 - * 6 2 / +
