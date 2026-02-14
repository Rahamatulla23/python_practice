class Dog:
    def __init__(self):
        self.name = 'Pummy'
        self.gender = 'Female'
        self.height = 2.5
        self.weight = 20
        self.color = 'Black'
        self.lifespan = 14
    
    def bark(self):
        print(f"{self.name} is Barking...")
    
    def details(self):
        print(f"Hello I am {self.name}")
        print(f"I have a life span of {self.lifespan} years")
        print(f"I am {self.color} in color")

d1 = Dog()
d1.bark()
d1.details()
print(d1.gender)