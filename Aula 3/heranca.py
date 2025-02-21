class Carro:

    def __init__(self , marca , cor):
        self.marca = marca
        self.cor = cor
        self.velocidade = 0
        
    def buzinar(self):
        print(f'{self.marca} {self.cor}: BI BI!')

    def acelerar(self):
        self.velocidade += 10
        print(f"O {self.marca} acelerou para {self.velocidade}Km")


class CarroEletrico (Carro):
    def __init__(self , carro):
        super().__init__(carro.marca, carro.cor)
        self.bateria = 100

    def carro_jenrico(self):
        self.__init__(Carro("qualquer", "Preto"))
    
    def acelerar(self):
        if self.bateria >= 10:
            super().acelerar()
            self.bateria = self.bateria*0.75
            print(f"A bateria caiu para {self.bateria}%")
        else:
            print("O carro nao pode acelerar pois esta com menos de 10% de bateria")


fusca = Carro("volkswagen", "Azul")

FuscaEletrico = CarroEletrico(fusca)

for i in range(10):
    FuscaEletrico.acelerar()
