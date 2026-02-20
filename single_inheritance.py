class Father:
    def methodA(self):
        print("This Method is in Father's Class")

class Son(Father):
    def methodB(self):
        print("This Method is in Son's Class")

obj = Son()
obj.methodA()
obj.methodB()