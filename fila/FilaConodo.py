from Nodo import Nodo

class FilaConodo:
    def __init__(self):
        self._primeiroFila = None
        self._ultimoFila = None
        self._tamanhoFila = 0

    def enfileirar(self, valor):
        novoNodo = Nodo(valor)
        #se a fila está vazia 
        if self._primeiroFila is None:
            self._primeiroFila = novoNodo
            self._ultimoFila = novoNodo
            self._tamanhoFila += 1
        else:#Se não está vazia
            self._ultimoFila.definirProximo(novoNodo)
            novoNodo.definirAnterior(self._ultimoFila)
            self._ultimoFila = novoNodo
            self._tamanho += 1
    
    def desenfileirar(self):
        if self._primeiroFila is None:
            return None
        else:
            valor = self._primeiroFila.obterValor()
            self._primeiroFila = self._primeiroFila.obterProximo()
            if self._primeiroFila is not None:
                self._primeiroFila.definirAnterior(None)
            else:
                self._ultimoFila = None
            self._tamanhoFila -= 1
            return valor


         




            
