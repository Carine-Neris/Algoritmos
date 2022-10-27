
class No:
  def __init__(self, valor):
    self._valor = valor
    self.proximo = None
    self.anterior = None

  def __str__(self):
    return str(f"{self._valor}")

  def __repr__(self):
    return repr(f"{self._valor}")