class Nodo:
    def __init__(self):
        self._valor = None
        self._proximo = None
        self._anterior = None
    
    def __init__(self, valor):
        self._valor = valor
        self._proximo = None
        self._anterior = None

    def definirProximo(self, proximo):
        self._proximo = proximo
    
    def definirAnterior(self, anterior):
        self._anterior = anterior
    
    def obterProximo(self):
        return self._proximo

    def obterAnterior(self):
        return self._anterior
    
    def definirValor(self, valor):
        self._valor = valor

    def obterValor(self):
        return self._valor

    

