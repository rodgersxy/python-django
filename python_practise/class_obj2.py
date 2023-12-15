# so can we create more than one object in a class?
# the answer is that, that is the whole idea, the class acts as a blueprint or template for the object

class Employee:
   def display(self):
       print("Hello, more than one object")
emp_obj1 = Employee()
emp_obj1.display()
emp_obj2 = Employee()
emp_obj2.display()