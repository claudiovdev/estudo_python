#Criando Tupla
lanche = ('Hamburger', 'Suco', 'Pizza','Pudim')

#Consultado um suco dentro da tupla
print(lanche[1])

for produto in lanche:
    if produto == 'Suco':
        print(f'Vou beber {produto}')
    else:
        print(f'Comi muito {produto}')