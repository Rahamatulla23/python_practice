'''
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print percentage of class attended
Is student is allowed to sit in exam or not.
'''
held=int(input("ENTER HOW MANY CLASS HELD: "))
attended=int(input("enter how many classes attended: "))
Percentage = (attended/held)*100
print("Attendance Percentage = {:.2f} %".format(Percentage))
if Percentage>=75:
    print("yoy can write exam")
else:
    print("you can't write exam")
    

