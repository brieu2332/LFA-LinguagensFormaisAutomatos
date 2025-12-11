class GeradorDeEstados:
    def __init__(self, prefixo='q'):
        self.contador = 0
        self.prefixo = prefixo
    
    def novo_estado(self):
        nome_estado = f"{self.prefixo}{self.contador}"
        self.contador += 1
        return nome_estado