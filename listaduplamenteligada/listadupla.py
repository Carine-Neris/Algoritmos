from no import *

class ListaDupla:
  def __init__(self, capacidade):
    self._capacidade = capacidade
    self._inicio = self._fim = None
    self._tamanho = 0
    print(f"Lista Duplamente Ligada criada com capacidade = {self._capacidade}")


  def l_vazia(self, print_str=False):  # self._inicio.proximo == self._fim
    if print_str:
      print("A lista está VAZIA!")
    return True if (self._inicio == None) else False
  
  
  def l_cheia(self, print_str=False):
    if print_str:
      print("A lista está Cheia!")
    return True if (self._tamanho == self._capacidade) else False
  
  
  def listar(self):
    if self.l_vazia():
      print('A lista não possui elementos para serem mostrados!')
    else:
      iterador = self._inicio
  
      while iterador is not None:
        print(f'Item: {iterador}')
        iterador = iterador.proximo
    
  def remover(self, removido):  # caso 1 - lista vazia 
    if self.l_vazia():
      print('Lista vazia, não existem elementos para serem removidos!')
    else:
      # caso 2 - elemento único
      if ((self._tamanho == 1) and (self._inicio._valor == removido)):
        self._inicio = self._fim = None
        self._tamanho -= 1
        print(f'Nó {removido} removido da lista!')
      else:
        # caso 3 - valor que será removido é o primeiro, mas existem outros valores
        if ((self._inicio._valor == removido) and (self._tamanho > 1)):
          self._inicio = self._inicio.proximo
          self._inicio.anterior = None
          self._tamanho -= 1
          print(f'Nó {removido} removido da lista!')
        else:
          # caso 4 - valor a ser removido é o último
          if (self._fim._valor == removido):
            self._fim = self._fim.anterior
            self._fim.proximo = None
            self._tamanho -= 1
            print(f'Nó {removido} removido da lista!')
          else:
            iterador = self._inicio
            while (iterador.proximo is not None):
              if iterador._valor == removido:
                iterador.anterior.proximo = iterador.proximo
                iterador.proximo.anterior = iterador.anterior
                self._tamanho -= 1
                print(f'Nó {removido} removido da lista!') 
                break 
              else:
                iterador = iterador.proximo
                if iterador.proximo == None:
                  print(f'Tentativa de remoção falhou!Elemento {removido} não encontrado!')
                     
        
  def add(self, node): 
    if self.l_vazia(): # caso - lista vazia
      self._inicio = node
      self._fim = node
      self._tamanho += 1
      print(f'Nó {node} adicionado na lista!') # caso - lista cheia
    else:
      if self.l_cheia():
        print(f'Capacidade máxima de {self._capacidade} atingida.Não é possível adicionar {node}!')
      else: 
        iterador = self._inicio
        # caso 2 - valor menor ou igual ao primeiro elemento da lista
        if (node._valor <= iterador._valor):
          node.proximo = self._inicio
          self._inicio.anterior = node
          self._inicio = node
          self._tamanho += 1
          print(f'Nó {node} adicionado na lista!')
        else:  
          # caso 4 - valor a ser inserido é maior que o último elemento da lista        
          if (node._valor > self._fim._valor):
              node.anterior = self._fim
              self._fim.proximo = node
              self._fim = node
          else: # caso 3 - valor a ser inserido é menor ou igual ao e-nesimo elemento da lista
            #iterador = self._inicio
            
            while ((iterador.proximo is not None) and (iterador._valor < node._valor)):
              iterador = iterador.proximo

            node.proximo = iterador
            node.anterior = iterador.anterior
            iterador.anterior.proximo = node
            iterador.anterior = node
          self._tamanho += 1
          print(f'Nó {node} adicionado na lista!')
       
      
      
      
    

    

    
    


