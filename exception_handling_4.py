print("Start")
try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    c = a/b
except:
    print("Exception Occured")
else:
    print(c)
finally:
    print("The End")