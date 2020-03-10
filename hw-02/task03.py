"""
Задача 3
В этой задаче вам необходимо создать объектную модель лыжника, спускающегося с горы. Лыжник может спускаться с горы в произвольном направлении. 
Однако, для определенности положим, что он может перемещаться только в 3-х направлениях: Юг, Запад, Восток. 
При этом, если он идет галсами в направлении Запад или Восток, то его скорость составляет 1 м/с, а если катится прямо вниз (Юг), то скорость выше, и равна 5 м/с.
Создайте программную модель движения лыжника и определите: 1) какое расстояние он проедет через 17 секунд спуска, 
если каждую секунду он меняет направление движения случайным образом, и 2) в каком направлении он двигался каждую секунду.
Приложение должно состоять из двух классов. Первый класс наполните характеристиками и методами лыжника. Второй класс используйте для параметров движения. 
Управление программой и вывод результатов производите в основной функции main.
"""
import math as m
import random as r

class Move(object):
  direction = ['South', 'West', 'East']
  delta_x = 0
  delta_y = 0

  def __init__(self, x, y, time):
    self.x = x
    self.y = y
    self.time = time

  def fun1(self, direc = ''):
    self.direc = direc  
    for n in range(self.time): 
      self.direc = r.choice(self.direction)     
      if self.direc == 'South':
        self.delta_y = self.y + 5
      if self.direc == 'West':
        self.delta_x = self.x - 1
      if self.direc == 'East':
        self.delta_x =  self.x + 1
      print(n,'second, direction -',self.direc)

  def way(self): #расстояние
    return m.sqrt((self.x + self.delta_x) ** 2 + (self.y + self.delta_y) ** 2) 

  def fun2(self):
    return self.delta_x, self.delta_y


class Skier(Move):
  def __init__(self, name, x = 0, y =0, time = 0):
    self.name = name
    super().__init__(x, y, time)

f = Skier('Ann', 0, 0, 17)

f.fun1()
f.fun2()
f.way()
