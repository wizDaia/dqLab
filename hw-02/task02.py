"""
Задача 2
Реализуйте класс товар, в который включите свойства и методы общие для любого товара из магазина бытовой электроники (не менее двух свойств и методов). 
Реализуйте двух наследников товара, например, классы телевизор и холодильник, 
которые должны будут иметь в дополнение к наследуемым хотя бы по одному собственному уникальному свойству и методу.
Пополните ассортимент своего виртуального магазина несколькими разными товарами с различными параметрами. 
Рассчитайте среднюю цену всех созданных товаров, используя главный класс. 
Реализуйте корректное сравнение двух товаров между собой по их исключительному свойству, 
например, два объекта-телевизора будут считаться равными между собой, если у них одинаковая диагональ.
Сравните несколько товаров между собой.
"""

class Goods(object):
  goodQuality = True
  store = 'Amazon'
  list = []

  def __init__(self, brand, quantity, price):
    self.brand = brand
    self.quantity = quantity
    self.__class__.list.append(price)

  def just(self):
    return 'This is %s' %(self.brand)
  
  def just2(self):
    return self.quantity
  
  @staticmethod
  #avg_price
  def func(): 
    return sum(Goods.list)/len(Goods.list)


class TV(Goods):
  department = 'electronics'

  def __init__(self, color, brand= 'hell', quantity = 0, price = 0):
    super().__init__(brand, quantity, price) 
    self.color = color

  def setValues(self, display):
    self.d = display

  def telev(self):
    return (self.brand, self.display, self.price)

  def __eq__(self, other):
    if isinstance(other, TV):
      return (self.d == other.d)
    return NotImplemented

class Fridge(Goods):
  department = 'kitchen'
  frozen = True

  def __init__(self, color, brand = 'LG', quantity = 0, price = 0):
    super().__init__(brand, quantity, price) 
    self.color = color

  def setValues(self, degrees):
    self.de = degrees

  def cold(self):
    return('This fridge %s colder than Russia at %s') %(self.brand, self.degrees)

  def __eq__(self, other):
    if isinstance(other, Fridge):
      return (self.de == other.de)
    return NotImplemented

g1 = Fridge('white', 'Samsung', 40, 5000)

g2 = TV('dark', 'Apple', 10, 10000)

g3 = TV('blue', 'LG', 12, 1000)

g4 = Fridge('black', 'IceAge', 500, 10800)

Goods.func()

g4.setValues(77)
g1.setValues(77)
print(g1 == g4)

g2.setValues(55)
g3.setValues(30)
print(g2 == g3)
