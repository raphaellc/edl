class Node:
    """
    Um Nodo em uma lista encadeada.
    """
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nodo
        self.proximo = None  # Referência para o próximo nodo
    