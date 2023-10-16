usuario_data_science = {15,23,43,56}
usuarios_machine_learning = {13,23,56,42}

#assistiram = usuario_data_science.copy()
#assistiram.extend(usuarios_machine_learning)
#lista_corrigida = set(assistiram)
#print(lista_corrigida)

print(usuario_data_science | usuarios_machine_learning)
print(usuario_data_science & usuarios_machine_learning)
print(usuario_data_science - usuarios_machine_learning)