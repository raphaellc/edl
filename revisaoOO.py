class Animal:
    """Classe base para animais."""

    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        """Método para emitir o som do animal."""
        print("Som genérico de animal.")

    def __str__(self):
        """Retorna uma representação em string do animal."""
        return f"{self.nome} ({self.especie})"


class Cachorro(Animal):
    """Classe que representa um cachorro, herdando de Animal."""

    def __init__(self, nome, raca):
        super().__init__(nome, especie="Cachorro")
        self.raca = raca

    def emitir_som(self):
        """Método para o cachorro latir."""
        print("Au au!")

    def __str__(self):
        """Retorna uma representação em string do cachorro."""
        return f"{self.nome} ({self.especie}, {self.raca})"


class Gato(Animal):
    """Classe que representa um gato, herdando de Animal."""

    def __init__(self, nome, cor):
        super().__init__(nome, especie="Gato")
        self.cor = cor

    def emitir_som(self):
        """Método para o gato miar."""
        print("Miau!")

    def __str__(self):
        """Retorna uma representação em string do gato."""
        return f"{self.nome} ({self.especie}, {self.cor})"


# Exemplo de uso
animal1 = Animal("Animal Genérico", "Desconhecida")
cachorro1 = Cachorro("Rex", "Pastor Alemão")
gato1 = Gato("Mingau", "Preto")

print(animal1)
animal1.emitir_som()

print(cachorro1)
cachorro1.emitir_som()

print(gato1)
gato1.emitir_som()

# Demonstração de polimorfismo
animais = [animal1, cachorro1, gato1]

print("\nDemonstração de polimorfismo:")
for animal in animais:
    print(f"{animal}: ", end="")
    animal.emitir_som()