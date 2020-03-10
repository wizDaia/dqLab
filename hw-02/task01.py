"""
Задача 1
Смоделируйте прием успешно окончивших тренинг студентов на работу в EPAM.
Вам необходимо будет реализовать класс Student, будущие создаваемые объекты которого описываются именем, фамилией, возрастом, 
а также по умолчанию знают английский язык. Также реализуйте в классе следующие методы: зачисление на курс (вызывается автоматически при создании объекта), 
обучение (в результате работы которого студенты помимо английского языка, смогут пополнить свой багаж знаний еще такими хард-скиллами, как SQL, Linux и Python), 
прием на работу (отрабатывает успешно, если студент обладает всеми необходимыми скиллами).
Создайте трех разных студентов. Двоих студентов обучите всем скиллам. Третий, к всеобщему сожалению, не выучит Python. Попробуйте принять всех троих на работу.
"""

class Student:
  eng = True
 
  def __init__(self, n, s, a):
    self.name = n
    self.surname = s
    self.age = a
 
  def __str__(self):
    return "Student %s %s has admitted to courses" %(self.name, self.surname)

  def setSkills(self, s1, s2, s3):
      self.sql = s1
      self.linux = s2
      self.python = s3

  def work(self):
      if self.sql == True and self.linux == True and self.python == True and self.eng == True:
          print("Job offer")
      else:
          print("Unable to job offer")


student1 = Student('John', 'Smith', 35)
print(student1)
student1.setSkills(True, True, False)
student1.work()

student2 = Student('Jennyfer', 'Jobs', 20)
print(student2)
student2.setSkills(True, True, True)
student2.work()

student3 = Student('Casper', 'The little ghost', 1000)
print(student3)
student3.setSkills(True, True, True)
student3.work()
