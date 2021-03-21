class Employee:
  #def get_info(self):
   # return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children
  def get_net_salary(self):
      tax = self.salary * 0.15 - self.children*1500
      net_salary = self.salary - tax
      return net_salary

employee1 = Employee("Martin", "účetní", 27000, 2)
print(employee1.get_net_salary())



