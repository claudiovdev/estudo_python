aparicoes = {"Vinicius": 1, "Fran": 2, "Caio": 3, "Rodrigo": 4}

aparicoes['Sula'] = 5

del aparicoes["Sula"]

print("Fran" in aparicoes)
print(" ")

for elemento in aparicoes.values():
    print(elemento)

print(" ")

for elemento in aparicoes.keys():
    print(elemento)

print(" ")

for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

print(" ")

for elemento in  aparicoes.items():
    print(elemento)

print(" ")

for chave, valor in aparicoes.items():
    print(chave, " ", valor
          )
