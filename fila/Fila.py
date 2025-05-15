class Fila:
    def __init__(self):
        self.dados = []
    
    def enfileirar(self, valor):
        self.dados.append(valor)
    
    def desenfileirar(self):
        self.dados.pop(0)

    def desenfileirarPorValor(self, valor):
        for i in range(len(self.dados)):
            if self.dados[i] == valor:
                self.dados.pop(i)
                break

    def mostrar(self):
        print(self.dados)
    
    def tamanho(self):
        print(len(self.dados))
    
    def vazia(self):
        print(len(self.dados) == 0)

    def buscarPorValor(self, valor):
        for i in range(len(self.dados)):
            if self.dados[i] == valor:
                return self.dados[i]

def main():
    fila = Fila()
    fila.mostrar()
    fila.enfileirar(4)
    fila.mostrar()
    fila.enfileirar(2)
    fila.mostrar()
    fila.desenfileirar()
    fila.mostrar()
    fila.enfileirar(5)
    fila.mostrar()
    fila.desenfileirarPorValor(2)
    fila.mostrar()



main()