from calendar import *

year = int(input("Enter Year: "))

if isleap(year):
    print("Leap Year")
else:
    print("Not a Leap Year")
