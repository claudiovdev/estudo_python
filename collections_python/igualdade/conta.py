class Conta:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def __eq__(self, other):
        if self.codigo == other.codigo:
            return True

    def __str__(self):
        return f'o Codigo da conta é: {self.codigo} e o saldo é: {self.saldo}'


conta1 = Conta(12)
conta2 = Conta(12)

resultado = conta1.__eq__(conta2)

print(resultado)
