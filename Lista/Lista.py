from turtle import clear
from typing import Optional, List
from Node import Node

class Lista:
    """
    Uma lista encadeada.
    """

    def __init__(self):
        self._nodo_inicial: Optional['Node'] = None  
        self._tamanho: int = 0  
        self._nodo_final: Optional['Node'] = None  

    def inserir(self, valor) -> None:
        """
        Insere um novo nodo no final da lista de forma recursiva.
        """
        self._inserir_recursivo(self._nodo_inicial, valor)

    def _inserir_recursivo(self, nodo: Optional['Node'], valor) -> None:
        if nodo is None:
            self._nodo_inicial = Node(valor)
            self._nodo_inicial.definir_proximo(self._nodo_inicial)
            self._tamanho += 1
            return
        if nodo.obter_proximo() is self._nodo_inicial:
            novo_node = Node(valor)
            novo_node.definir_proximo(self._nodo_inicial)
            nodo.definir_proximo(novo_node)
            self._tamanho += 1
            return

        else:
            self._inserir_recursivo(nodo.obter_proximo(), valor)

    def busca(self, valor) -> Optional[int]:
        """
        Busca o primeiro nodo com o valor fornecido e retorna a posição.
        Retorna None se o valor não for encontrado.
        """
        return self._busca_recursiva(self._nodo_inicial, valor, 0)

    def _busca_recursiva(self, nodo: Optional['Node'], valor, posicao: int) -> Optional[int]:
        if nodo is None:
            return None  # Retorna None para indicar que o valor não foi encontrado
        if nodo.obter_valor() == valor:
            return posicao
        return self._busca_recursiva(nodo.obter_proximo(), valor, posicao + 1)

    def remover_por_posicao(self, posicao: int) -> None:
        """
        Remove o nodo na posição especificada.
        """
        if self._nodo_inicial is None:
            raise IndexError("A lista está vazia.")
        if posicao == 0:
            self._nodo_inicial = self._nodo_inicial.obter_proximo()
        else:
            self._remover_por_posicao_recursivo(self._nodo_inicial, posicao, 1)

    def _remover_por_posicao_recursivo(self, nodo: Optional['Node'], posicao: int, contador: int) -> None:
        if nodo is None or nodo.obter_proximo() is None:
            raise IndexError("Posição fora do alcance da lista.")
        if contador == posicao:
            nodo.definir_proximo(nodo.obter_proximo().obter_proximo())
        else:
            self._remover_por_posicao_recursivo(nodo.obter_proximo(), posicao, contador + 1)

    def remover_por_valor(self, valor) -> bool:
        """
        Remove o primeiro nodo com o valor especificado.
        Retorna True se o valor for removido, False caso contrário.
        """
        return self._remover_por_valor_recursivo(self._nodo_inicial, valor)

    def _remover_por_valor_recursivo(self, nodo: Optional['Node'], valor) -> bool:
        if nodo is None:
            return False
        if nodo.obter_proximo() is not None and nodo.obter_proximo().obter_valor() == valor:
            nodo.definir_proximo(nodo.obter_proximo().obter_proximo())
            self._tamanho -= 1
            return True
        else:
            return self._remover_por_valor_recursivo(nodo.obter_proximo(), valor)

    def obterTamanhoLista(self) -> int:
        return self._tamanho

    def __str__(self) -> str:
        """
        Retorna uma representação em string da lista encadeada.
        """

        def elementos_recursivos(nodo: Optional['Node']) -> List[str]:
            if nodo is None:
                return []
            return [str(nodo.obter_valor())] + elementos_recursivos(nodo.obter_proximo())

        return "[" + ", ".join(elementos_recursivos(self._nodo_inicial)) + "]"