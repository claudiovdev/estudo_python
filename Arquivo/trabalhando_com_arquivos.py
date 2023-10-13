#Criando arquivo
#arquivo = open("palavras.txt", "a")

#arquivo.write("Banata\n")
#arquivo.write("Melancia\n")

#arquivo.close()


#Lendo o arquivo
arquivo = open("palavras.txt", "r")

for cada in arquivo:
    print(cada)