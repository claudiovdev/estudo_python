from conta import Conta

from cliente import Cliente

conta = Conta(123, "Vinicius", 50.0, 100.0)
conta1 = Conta(1, "Fulano", 0.0,2000.0)
conta2 = Conta(2, "Beltrano", 0.0, 2000.0)
conta3 = Conta(3, "Sicrano", 0.0, 2000.0)


conta.transfere(conta2,5.0)


print(conta.codigo_banco)



cliente = Cliente("Vinicius")

print(cliente.nome)