from datetime import datetime

class ContaBancaria:
    
    def __init__(self , saldo):
        self.__saldo = saldo if saldo > 0 else 0
        self.__extrato = []
        self.lancarMovimentacao(f"Saldo inicial: {self.__saldo}" , "Abertura de conta" , "" )

    def lancarMovimentacao(self, valor, tipo, observação):
        self.__extrato.append({ 
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "obs" : observação,
            "valor" : valor,
            "tipo" : tipo
            }) 
        
    def depositar(self, valor, obs):
        self.__saldo += valor
        self.lancarMovimentacao(f"{valor}: Saldo final {self.__saldo}", "deposito" , obs)

    def sacar(self, valor, obs):
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.lancarMovimentacao(f"{valor}: Saldo final {self.__saldo}", "saque" , obs)
        else:
            msg = "tentativa de movimentação nâo autorizada, valor do saldo insuficiente"
            print(msg)
            self.lancarMovimentacao(f"{valor}: Saldo atual {self.__saldo}", "saque" , msg)
            
    def ver_saldo(self):
        print(f"seu saldo é de: {self.__saldo}")       

    def ver_extrato(self):
        print("extrato:")
        [print(x) for x in self.__extrato] 



conta = ContaBancaria(10)

conta.ver_saldo()
conta.depositar(100, "salario")
conta.ver_saldo()
conta.sacar(200, "saque emergencial")
conta.ver_saldo()
conta.ver_extrato()
