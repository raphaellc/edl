from Lista import Lista

# Código de teste
def main():
    lista = Lista()
    lista.inserir(10, 0)
    lista.inserir(20, 1)
    lista.inserir(30, 2)
    lista.inserir(15, 1)
    print("Lista após inserções:", lista)
    
    print("Posição do elemento 20:", lista.busca(20))
    print("Posição do elemento 100:", lista.busca(100))  # Não existe na lista
    
    lista.remover(1)
    print("Lista após remoção na posição 1:", lista)
    
    lista.remover(0)
    print("Lista após remoção na posição 0:", lista)

if __name__ == "__main__":
    main()
