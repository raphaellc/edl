from Node import Node
class Lista:
    """
    Uma lista encadeada.
    """
    def __init__(self):
        self.nodo_inicial = None  # Cabeça da lista encadeada
        self.tamanho = 0  # Número de elementos na lista
        

    def inserir(self, valor):
        """
        Insere um novo nodo no final da lista de forma recursiva.
        """
        def inserir_recursivo(nodo, valor):
            if nodo.proximo is None:
                nodo.proximo = Node(valor)
                self.tamanho += 1
            else:
                inserir_recursivo(nodo.proximo, valor)
        
        if self.nodo_inicial is None:
            self.nodo_inicial = Node(valor)
            self.tamanho += 1
        else:
            inserir_recursivo(self.nodo_inicial, valor)

    def busca(self, valor):
        """
        Busca o primeiro nodo com o valor fornecido e retorna a posição.
        Retorna -1 se o valor não for encontrado.
        """
        def busca_recursiva(nodo, valor, posicao):
            if nodo is None:
                return -1
            if nodo.valor == valor:
                return posicao
            return busca_recursiva(nodo.proximo, valor, posicao + 1)
        
        return busca_recursiva(self.nodo_inicial, valor, 0)

    def remover(self, posicao):
        """
        Remove o nodo na posição especificada.
        """
        def remover_recursivo(nodo, posicao):
            if nodo is None or nodo.proximo is None:
                raise IndexError("Posição fora do alcance da lista.")
            if posicao == 1:
                nodo.proximo = nodo.proximo.proximo
            else:
                remover_recursivo(nodo.proximo, posicao - 1)
        
        if self.nodo_inicial is None:
            raise IndexError("A lista está vazia.")
        if posicao == 0:
            self.nodo_inicial = self.nodo_inicial.proximo
        else:
            remover_recursivo(self.nodo_inicial, posicao)
    
    def obterTamanhoLista(self) -> int:
        return self.tamanho
        
    def __str__(self):
        """
        Retorna uma representação em string da lista encadeada.
        """
        def elementos_recursivos(nodo):
            if nodo is None:
                return []
            return [str(nodo.valor)] + elementos_recursivos(nodo.proximo)
        
        return "[" + ", ".join(elementos_recursivos(self.nodo_inicial)) + "]"
