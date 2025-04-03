from Lista import Lista  # Assuming Lista class is in Lista.py

# Código de teste
def main():
    lista = Lista()
    lista.inserir(10)
    lista.inserir(20)
    lista.inserir(30)
    lista.inserir(15)
    lista.inserir(50)
    lista.inserir(40)
    

    print("Lista após inserções:", lista)

    print("Posição do elemento 30:", lista.busca(30))
    print("Posição do elemento 100:", lista.busca(100))  # Não existe na lista

    # Removendo por posição (refatorado)
    try:
        lista.remover_por_posicao(1)  # Using the correct method name
        print("Lista após remoção na posição 1:", lista)
    except IndexError as e:
        print(f"Erro ao remover na posição 1: {e}")

    try:
        lista.remover_por_posicao(0)  # Using the correct method name
        print("Lista após remoção na posição 0:", lista)
    except IndexError as e:
        print(f"Erro ao remover na posição 0: {e}")

    # Removendo por valor
    removido = lista.remover_por_valor(40)
    if removido:
        print("Lista após remover o valor 20:", lista)
    else:
        print("Valor 20 não encontrado na lista.")

    removido = lista.remover_por_valor(50)
    if removido:
        print("Lista após remover o valor 50:", lista)
    else:
        print("Valor 50 não encontrado na lista.")

if __name__ == "__main__":
    main()