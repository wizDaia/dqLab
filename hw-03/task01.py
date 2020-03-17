import math as m


class PreconditionError(Exception):
  def __init__(self, *args):
    self.args = args

  def __str__(self):
    return f'Исключение: нарушение предусловия'

class ComplexRootError(Exception):
  def __init__(self, *args):
    self.args = args

  def __str__(self):
    return f'Исключение: комплексные корни'


def solve(a, b, c):
  try:
    for i in [a, b, c]:
      if i == int(i) or i == float(i):
        pass
      else:
        raise TypeError(i)
    if a == 0:
      raise PreconditionError
    else:
      D = b ** 2 - 4 * a * c
      print(D)
      if D < 0:
        raise ComplexRootError(a, b, c)
      if D == 0:
        x1 = -b / (2 * a)
        print(float(x1))
      if D > 0:
        x1 = (-b + m.sqrt(D)) / (2 * a)
        x2 = (-b - m.sqrt(D)) / (2 * a)
        print(float(x1), float(x2))
  except ComplexRootError as err:
    print(err)
  except PreconditionError as err:
    print(err)
  except TypeError as err:
    print('Исключение: неправильные типы', err.args[0])
  except Exception as err:
    print(type(err), err)
