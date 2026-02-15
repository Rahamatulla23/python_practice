class Student:
   def __init__(self):
        self.name = 'Vishnu'
        self.age = 22
        self.marks = 897
      
   def talk(self):
       print(f"Hai I am {self.name}")
       print(f"My Age is {self.age}")
       print(f"My Marks are {self.marks}")

s1 = Student()
s1.talk()
print("----------------------------")
s2 = Student('Chandrakanth')
s2.talk()