
contNumDigitados = 0
resultado = 0
while True:
    numero = int(input("Digite um numero: , (Utilize o 999 para parar): "))
    if numero == 999:
        break
    contNumDigitados = contNumDigitados + 1
    resultado = resultado + numero
print(f'A soma dos {contNumDigitados} numeros é igual a {resultado}')
