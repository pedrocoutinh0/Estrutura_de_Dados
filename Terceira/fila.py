class No:
    """Esta classe representa um nó de uma lista encadeada."""
    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.prox = proximo

class Fila:
  # cria fila vazia
  def __init__(fila):
    fila.inicio = None
    fila.fim = None

  def vazia(fila):
    return fila.inicio
    
  def enfileirar(fila, novo_dado):
    novo_no = No(novo_dado)

    if fila.inicio == None :
      fila.inicio = novo_no
    else:
      fila.fim.prox = novo_no
    fila.fim = novo_no

  # funciona somente se a fila não é vazia
  def desenfileirar(fila):
    primeiro = fila.inicio
    dado = primeiro.dado

    fila.inicio = fila.inicio.prox
    if fila.inicio==None:
      fila.fim = None

    return dado