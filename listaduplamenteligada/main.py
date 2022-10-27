from listadupla import *

listadupla = ListaDupla(6)    #capacidade 6
print("")

print("--------Listando os elementos da Lista Duplamente ligada!--------\n")
listadupla.listar()
print("")
print("-----------Lista Vazia? -----------\n")
listadupla.l_vazia(True)
print("")

print("-----------Inserindo elementos-----------\n")
listadupla.add(No(2))
listadupla.add(No(1))
listadupla.add(No(4))       
listadupla.add(No(5)) 
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("-----------Inserindo elementos-----------\n")
listadupla.add(No(3)) 
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("-----------Inserindo elementos-----------\n")
listadupla.add(No(9)) 
print("")

listadupla.add(No(8))  # Capacidade máxima atingida = 6
print("")

print("")
print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("--------Removendo item da Lista!--------\n")
listadupla.remover(1)
print("")

print("-----------Inserindo elementos-----------\n")
listadupla.add(No(8))
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()

print("--------Removendo item da Lista!--------\n")
listadupla.remover(1)
print("")

print("--------Removendo item da Lista!--------\n")
listadupla.remover(8)
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("-----------Inserindo elementos-----------\n")
listadupla.add(No(9)) 
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("--------Removendo item da Lista!--------\n")
listadupla.remover(9)
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("--------Removendo item da Lista!--------\n")
listadupla.remover(9)
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("--------Removendo item da Lista!--------\n")
listadupla.remover(2)
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("-----------Inserindo elementos-----------\n")
listadupla.add(No(10))
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("------------Testando capacidade máxima!------------")
print("-----------Inserindo elementos-----------\n")
listadupla.add(No(1))
listadupla.add(No(2))
listadupla.add(No(11)) #capacidade máxima atingida (6)
print("")

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("------------Testando remover da lista vazia!------------")
print("--------Removendo item da Lista!--------\n")
listadupla.remover(1)
listadupla.remover(2)
listadupla.remover(11) # elemento não encontrado
listadupla.remover(4)
listadupla.remover(5)

print("--------Listando os elementos da Lista!--------\n")
listadupla.listar()
print("")

print("--------Removendo item da Lista!--------\n")
listadupla.remover(10)
listadupla.remover(3) 
listadupla.remover(2) # lista vazia
print("")




