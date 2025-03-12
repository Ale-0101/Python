from dataclasses import dataclass

@dataclass
class Carro:
    marca : str
    cor : str
    cor : str = 0

    def __post_init__(self):
        if not isinstance(self.marca, str):
            raise TypeError(f"Esperado tipo 'str' para 'marca', mas recebeu {type(self.marca)}")
        if not isinstance(self.cor, str):
            raise TypeError(f"Esperado tipo 'str' para 'cor', mas recebeu {type(self.cor)}")
        

    def buzinar(self):
        print(f'{self.marca} {self.cor}: BI BI!')
    
    def acelerar(self):
        self.velocidade += 10
        print(f"O {self.marca} acelerou para {self.velocidade}Km")


fusca = Carro("volkswagen", "Azul")
jeep = Carro("Jeep", "Preto")

fusca.acelerar()
jeep.buzinar()