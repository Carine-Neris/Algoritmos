""" Recursão é quando uma função chama a si mesma  """

# Função recursiva
def contagem_regresiva(numero):
    print(numero)
    if numero > 0:
        numero = numero - 1
        contagem_regresiva(numero)
    else:
        print("A contagem regressiva terminou")


numero = int(input("Por onde a contagem regresiva deve iniciar? "))
contagem_regresiva(10)
