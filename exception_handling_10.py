print("Start")
try:
    a = int(input("Enter a Value: "))
    b = int(input("Enter b Value: "))
    c = a/b
except (ValueError, ZeroDivisionError):
    print("Exception: Please provide integer value only or ")
    print("Denominator should not be Zero")
else:
    print(c)
finally:
    print("The End")