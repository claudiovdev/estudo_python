
valorTabuada = 0;
while valorTabuada >= 0:
    contadorTabuada = 0;
    valorTabuada = int(input("Quer ver a tabuada de qual valor: "))
    if valorTabuada < 0:
        break
    while contadorTabuada < 11:
        resultado = valorTabuada * contadorTabuada
        print(f'{valorTabuada} x {contadorTabuada} = {resultado}')
        contadorTabuada = contadorTabuada + 1
print("FIM")