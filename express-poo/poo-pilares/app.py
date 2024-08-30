class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado
    
    def depositar(self, valor):
        """Método público para depositar dinheiro na conta"""
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        """Método público para sacar dinheiro da conta"""
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def consultar_saldo(self):
        """Método público para consultar o saldo da conta"""
        return f"Saldo de {self.__titular}: R${self.__saldo:.2f}"

# Exemplo de uso

conta = ContaBancaria("Yago", 500)
print(conta.consultar_saldo())
print(" ")
conta.depositar(2.50)
print(conta.consultar_saldo()) #Yago vendeu uma trufa
print(" ")
conta.sacar(50) #Yago sacou dinheiro para comprar mais trufas
print(conta.consultar_saldo())
