class Student:
   def __init__(self, name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
      
   def talk(self):
       print(f"Hai I am {self.name}")
       print(f"My Age is {self.age}")
       print(f"My Marks are {self.marks}")

s1 = Student('Vishnu', 22, 897)
s1.talk()
print("-------------------------")
s2 = Student('Tarun', 28, 789)
s2.talk()