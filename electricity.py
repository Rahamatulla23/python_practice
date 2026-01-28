'''
Write a Python program to input electricity units and calculate total electricity bill according to the given condition:
For 50 units Rs. 2.65/unit
For 51-100 units Rs. 3.35/unit
For 101-200 units Rs. 5.40/unit
For unit above 200 Rs. 7.10/unit
An additional surcharge of 20% is added to the bill
'''
unite=int(input("ENTER used UNITS: "))
if 0<=unite>=50:
     bill=bill*2.65
elif 50<unite<=100:
     bill=50*2.65+(unite-50)*3.35
elif 100<unite<=200:
     bill=50*2.65+50*3.35(unite-100)*5.40
elif unite>200:
     bill=50*2.65+50*3.35+100*5.40(unite-200)*7.1
print("actual bill=",bill)
final_bill=bill+bill*0.2
print("the final bill is:",final_bill)