class Employee:
    def __init__(self):
        self.id = 78965
        self.name = 'Sundar Pichai'
        self.designation = 'CEO'
        self.salary = 76000000
        self.company = 'Google'
    
    def talk(self):
        print(f"Hai I'm {self.name}")
        print(f"I work for {self.company}")
        print(f"I earn {self.salary} per month")

sp = Employee()
sp.talk()