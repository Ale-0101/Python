from datetime import datetime

class ContaBancaria:
    
    def __init__(self , saldo):
        self.__saldo = saldo if saldo > 0 else 0
        self.__extrato = []
        self.lancarMovimentacao(0 , "Abertura de conta" , "" )

    def lancarMovimentacao(self, valor, tipo, observação):
        self.__extrato.append({ 
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "tipo" : tipo,
            "valor" : valor,
            "saldo" : self.__saldo,
            "obs" : observação,            
            }) 
        
    def depositar(self, valor, obs):
        self.__saldo += valor
        self.lancarMovimentacao(valor, "deposito" , obs)

    def sacar(self, valor, obs):
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.lancarMovimentacao(valor, "saque" , obs)
        else:
            msg = "tentativa de movimentação nâo autorizada, valor do saldo insuficiente"
            print(msg)
            self.lancarMovimentacao(valor, "saque" , msg)
            
    def ver_saldo(self):
        print(f"seu saldo é de: {self.__saldo}")       

    def ver_extrato(self):
        print("extrato:")
        [print(x) for x in self.__extrato] 



conta = ContaBancaria(100)

conta.ver_saldo()
conta.depositar(100, "salario")
conta.ver_saldo()
conta.sacar(200, "saque emergencial")
conta.ver_saldo()
conta.ver_extrato()
