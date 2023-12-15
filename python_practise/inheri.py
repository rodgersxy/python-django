class A:
   def __init__(self):
       print("super class A constructor")
class B(A):
   def __init__(self):
       print("Child class B constructor")
       super().__init__()
  
b=B() 