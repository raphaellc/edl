from Lista import Lista  # Assuming Lista class is in Lista.py

# Código de teste
def main():
    lista = Lista()
    lista.inserir(10)  # Changed: Inserting without position
    lista.inserir(20)
    lista.inserir(30)
    lista.inserir(15)
    print("Lista após inserções:", lista)

    print("Posição do elemento 20:", lista.busca(20))
    print("Posição do elemento 100:", lista.busca(100))  # Não existe na lista

    lista.remover(1)
    print("Lista após remoção na posição 1:", lista)

    lista.remover(0)
    print("Lista após remoção na posição 0:", lista)

if __name__ == "__main__":
    main()