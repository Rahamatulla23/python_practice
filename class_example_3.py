class Human:
    def __init__(self):
        self.name = 'Manisha'
        self.height = 5.6
        self.weight = 56
        self.age = 22
        self.gender = 'Female'
        self.place = 'Anantapur'
        self.insta_id = 'meriseymanisha'
    
    def display(self):
        print(f"Hola.. I'm {self.name}")
        print(f"I am native of {self.place}")
    
    def addition_details(self):
        print(f"I am {self.age} years old")
        print(f"My Height is {self.height}")
        print(f"My Weight is {self.weight}")
        print(f"I'll be available on {self.insta_id}")

obj = Human()
obj.display()
obj.addition_details()