


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def codigo_banco(self):
        return self.__codigo_banco

    @codigo_banco.setter
    def codigo_banco(self, codigo_banco):
        self.__codigo_banco = codigo_banco

    @saldo.setter
    def saldo(self, saldo):
         self.__saldo = saldo

    @titular.setter
    def titular(self, titular):
         self.__titular = titular

    @limite.setter
    def limite(self, limite):
         self.__limite = limite

    def pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)
    def extrato(self):
        print(f'Saldo {self.__saldo} do Titular {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Você não possue mais saldo nem limite de credito")

    def transfere(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
