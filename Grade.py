'''
Write a Python program to input marks of five subjects Physics, Chemistry, Biology., Mathenatics and Computer. Calculate percentage and grade according to following:
Percentage>=90%: Grade A
Percentage>=80%: Grade B
Percentage>=70%: Grade C
Percentage>= 60%: Grade D
Percentage>=40%: Grade E
Percentage<40%: Grade F
'''
Name=(input("ENTER STUDENT NAME: "))
Physics=int(input("ENTER Physics marks: "))
chemistry=int(input("ENTER Chemistery marks: "))
biology=int(input("ENTER Biology marks: "))
maths=int(input("ENTER Maths marks: "))
computer=int(input("ENTER computer marks: "))
total=Physics+chemistry+biology+maths+computer
Percentage=(total/500)*100
print("obtained percentage is = {:.2f}%".format(Percentage))

if Percentage>=90:
    print("You Got Grade A")
elif Percentage>=80:
    print("You Got Grade B")
elif Percentage>=70:
    print("You Got Grade C")
elif Percentage>=60:
    print("You Got Grade D")
elif Percentage>=40:
    print("You Got Grade E")
elif Percentage<40:
    print("You Got Grade F")
