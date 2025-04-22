""" Recursão é quando uma função chama a si mesma  """

# Função recursiva
def contagem_regressiva(numero):
    print(numero)
    if numero > 0:
        numero = numero - 1
        contagem_regressiva(numero)
    else:
        print("A contagem regressiva terminou")


numero = int(input("Por onde a contagem regressiva deve iniciar? "))
contagem_regressiva(numero)
