class ContaBancaria:

    def __init__(self , saldo):
        self.__saldo = saldo if saldo > 0 else 0
        
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Seu saldo é insuficiente para sacar este valor.")
            
    def ver_saldo(self):
        print(f"seu saldo é de: {self.__saldo}")       


conta = ContaBancaria(100)

conta.ver_saldo()
conta.depositar(100)
conta.ver_saldo()
conta.sacar(200)
conta.ver_saldo()
