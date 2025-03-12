import contador as Contador

class Votacao:
    def __init__(self, titulo, candidatos):
        self.titulo = titulo
        self.candidatos = {}
        for candidato in candidatos:
            self.candidatos[candidato] = Contador.Contador(candidato)
        self.votos = 0

    def votar(self, candidato):
        if candidato in self.candidatos:
            self.candidatos[candidato].incrementa()
            self.votos += 1
        else:
            print("Candidato inválido.")

    def exibir_resultados(self):
        print(f"Resultado da votação: {self.titulo}")
        print("---------------------------")
        for candidato, contador in self.candidatos.items():
            print(f"{candidato}: {contador.contagem()} votos")
        print(f"Total de votos: {self.votos}")

# Exemplo de uso:
if __name__ == "__main__":
    candidatos = ["Alice", "Bob", "Carlos"]
    votacao = Votacao("Eleição para Direção da Associação de Docentes da Unisinos", candidatos)

    # Simulação de votos
    votacao.votar("Alice")
    votacao.votar("Bob")
    votacao.votar("Alice")
    votacao.votar("Carlos")
    votacao.votar("Bob")
    votacao.votar("Bob")
    votacao.votar("Candidato Inválido") # Testando candidato inválido

    # Exibir resultados
    votacao.exibir_resultados()