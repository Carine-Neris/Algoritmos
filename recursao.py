""" Recursão é quando uma função chama a si mesma  """

# Função recursiva
def contagem_regresiva(n):
    print(n)
    if n > 0:
        n = n - 1
        contagem_regresiva(n)
    else:
        print("A contagem regressiva terminou")


contagem_regresiva(10)
