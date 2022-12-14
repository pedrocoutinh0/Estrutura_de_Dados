from pilha import Pilha

def eh_operador(c):
    if c == "+" or c == "-" or c == "*" or c == "/":
        return True
    else:
        return False


def precedencia(c):
    if c == "+" or c == "-":
        return 1
    elif c == "*" or c == "/":
        return 2
    else:
        return False


def toposfixa(infixa):
    pilha = Pilha()
    posfixa = ""
    for c in infixa:  # Percorrer a expressão infixa
        if not eh_operador(c) and not (c == "(" or c == ")"):  # Condição para colocar os operandos na expressão pós-fixa.
            posfixa += c
        if eh_operador(c):  # Condição que vai comparar a precedencia do operador com o topo da pilha.
            while not pilha.vazia() and precedencia(pilha.obter_topo()) >= precedencia(c):
                posfixa += pilha.desempilhar()
            pilha.empilhar(c)
        if c == "(":
            pilha.empilhar(c)
        if c == ")":
            while True:  # Laço que vai parar somente quando encontrar a abertura do parêntese e retirá-lo da pilha.
                if pilha.obter_topo() != "(":
                    posfixa += pilha.desempilhar()
                else:
                    pilha.desempilhar()
                    break
    while not pilha.vazia():  # Colocar o restante da pilha na expressão pós-fixa.
        posfixa += pilha.desempilhar()
    return posfixa
