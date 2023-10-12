frase = "Curso em Video Python"

#Retornando a primeira posição
print("Retornando a primeira posição ",frase[0])

#Retornando a entre primeira posição e a posição 9
print("Retornando a primeira posição ",frase[0:9])


#Retornando a entre primeira posição e a posição 9 e em seguida mostra tudo depois
print("Retornando a primeira posição ",frase[9:])

#Utilizando uma função para retornar quantidade de caracteres
print("A frase possute {} caracteres".format(len(frase)))

#Utilizando uma função para retornar quantidade de caracteres especifico
print("A frase encontrou {} vezes".format(frase.count('o')))

#Utilizando uma função para retornar em qual posição ele encontrou a frase
print("O texto está na posição  {}".format(frase.find('deo')))

#Utilizando uma função para alterar uma palavra da frase
print("A nova frase adicionada é {}".format(frase.replace("Python", "Android")))

#Utilizando uma função para colocar a frase em maiusculo
print("Adicionando frase para maiusculo {}".format(frase.upper()))

#Utilizando uma função para colocar a frase em minuscuçp
print("Adicionando frase para minusculo {}".format(frase.lower()))

#Utilizando uma função para deixar apenas a primeira letra em maiusculo
print("Adicionando apenas a primeira letra em maiusculo {}".format(frase.capitalize()))

#Utilizando uma função para alterar letra maiusculo após cada palavra
print("Colocando o inicio de cada palavra em maiusculo {}".format(frase.title()))

frase = "   Aprendendo Python  "

#Utilizando uma função para remover espaços inuteis
print("removendo espaços inuteis {}".format(frase.strip()))


#Utilizando uma função para remover espaços inuteis da direita
print("removendo espaços inuteis da direita {}".format(frase.rstrip()))

frase = "Curso em Video Python"

#Utilizando função para separar um teste em lista de objetos
fraseDividida = frase.split()
print("Mostrando os objetos após alteração posição 0: {}, posição 1: {}".format(fraseDividida[0], fraseDividida[1]))

