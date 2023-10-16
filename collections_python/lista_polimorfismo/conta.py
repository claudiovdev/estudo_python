from abc import ABCMeta, abstractmethod
class Conta:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'o Codigo da conta é: {self.codigo} e o saldo é: {self.saldo}'
