print("Start")
try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    c = a/b
except ValueError:
    print("Exception: Please provide integer value only")
except ZeroDivisionError:
    print("Exception: Denominator should not be Zero")
else:
    print(c)
finally:
    print("The End")