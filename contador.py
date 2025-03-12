class Contador:
    def __init__(self,id):
        self._id = id
        self._cont = 0
    def incrementa(self):
        self._cont += 1
    def contagem(self):
        return self._cont
    def obtemId(self):
        return self._id
    def __str__(self):
        return f"{self._id} - {self._cont}"
    
c1 = Contador(1)
c2 = Contador(2)
