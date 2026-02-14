class Student:
    def __init__(self):
        self.id = 1001
        self.name = 'Karun'
        self.age = 22
        self.marks = 892
        self.branch = 'CSE'

    def studying(self):
        print(f"Hello I am {self.name}")
        print(f"My Age is {self.age}")
        print(f"I belong to {self.branch} department")
        print(f"I have secured {self.marks} Marks in my +2")

s1 = Student()
s1.studying()