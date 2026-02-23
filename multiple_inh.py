class A(object):
    def methodA(self):
        print("This Method is in class A")

class B(object):
    def methodB(self):
        print("This Method is in class B")
class C(A,B):
    def methodC(self):
        print("This Method is in class C")


obj = C()
obj.methodA()
obj.methodB()
obj.methodC()
