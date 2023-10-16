class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'o Codigo da conta é: {self.codigo} e o saldo é: {self.saldo}'


conta_claudio = ContaCorrente(1)

#print(conta_claudio)

conta_claudio.deposito(1000)
#print(conta_claudio)

conta_fran = ContaCorrente(2)
conta_fran.deposito(2000)

##Depositando 100 em cada conta
contas = [conta_claudio, conta_fran]
for conta in contas:
    conta.deposito(100)

print(' ')
print('Realizando um for nas contas')
print(' ')
for conta in contas:
    print(conta)

##Depositando 100 em cada conta


