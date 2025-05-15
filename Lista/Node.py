from typing import Optional
class Node:
    """
    Um Nodo em uma lista encadeada.
    """

    def __init__(self, valor):
        self._valor = valor  # Valor armazenado no nodo
        self._proximo: Optional['Node'] = None  # Referência para o próximo nodo
       

    def obter_valor(self) -> any:
        return self._valor

    def definir_valor(self, valor) -> None:
        self._valor = valor

    def obter_proximo(self) -> Optional['Node']:
        return self._proximo

    def definir_proximo(self, proximo: Optional['Node']) -> None:
        self._proximo = proximo
    