class Student:
   def __init__(self, n ='', m=0): 
      self.name = n 
      self.marks = m 

   def display(self): 
      print('Hi', self.name) 
      print('Your marks', self.marks) 

s1 = Student() 
s1.display() 
print('------------------') 
s2 = Student('Meera Bai', 880) 
s2.display() 
