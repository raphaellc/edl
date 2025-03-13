class Veiculo:
    def __init__(self, roda, velocidade, tam_tanque):
        self._roda = roda
        self._velocidade = velocidade
        self._tam_tanque = tam_tanque
    
    def definirRoda(self, roda):
        self._roda = roda
    
    def definirVelocidade(self, velocidade):
        self._velocidade = velocidade
    
    def definirTamTanque(self, tam_tanque):
        self._tam_tanque = tam_tanque

    def obtemRoda(self):
        return self._roda
    
    def obtemVelocidade(self):
        return self._velocidade
    
    def obtemTamTanque(self):
        return self._tam_tanque
    
    def __str__(self):
        return f"{self._roda} {self._velocidade} {self._tam_tanque}"
    
class Carro(Veiculo):
    def __init__(self, roda, velocidade, tam_tanque, modelo):
        super().__init__(roda, velocidade, tam_tanque)
        self._modelo = modelo
    
    def definirModelo(self, modelo):
        self._modelo = modelo
    
    def obtemModelo(self):
        return self._modelo
    
    def obtemTamTanque(self):
        return self._tam_tanque *0.8