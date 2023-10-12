valor = 'S'
while valor == 'S':
    r = input("Digite um valor: ")
    valor = input("Deseja continuar: ").upper()
print("Fim, você digitou {}".format(valor))