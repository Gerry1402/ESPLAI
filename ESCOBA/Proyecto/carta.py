class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def __str__(self):
        nombres_valores = {1: "As", 8: "Sota", 9: "Caballo", 10: "Rey"}
        nombre_valor = nombres_valores.get(self.valor, str(self.valor))
        return f"{nombre_valor} de {self.palo.lower()}s"
    
    def __repr__(self) -> str:
        return f"{self.__str__()}"