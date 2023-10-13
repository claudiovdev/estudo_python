try:
    numero = int(input("Digite um numero: "))
    divisor = int(input("Digite um divisor: "))
    resultado = numero % divisor

except ZeroDivisionError:
    print("Erro não podemos realizar uma divisão com o divisor 0")

except ValueError:
    # Tratando a exceção específica quando o usuário não insere um número válido
    print("Erro: Por favor, insira um número válido.")

except Exception as e:
    # Tratando outras exceções genéricas
    print("Ocorreu um erro:", e)

else:
    # Este bloco é executado se nenhuma exceção for lançada
    print("Nenhuma exceção foi lançada.")

finally:
    # Este bloco é sempre executado, independentemente de exceções
    print("O código foi executado.")