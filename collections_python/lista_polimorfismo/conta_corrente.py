from collections_python.lista_polimorfismo.conta import Conta


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo += 2

class ContaSalario(Conta):
    pass


conta16 = ContaCorrente(16)

ContaSalario(10)
print(conta16)
