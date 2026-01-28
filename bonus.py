 #A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
bonus=float(input("ENTER YOUR SALARY: "))
serivice=int(input("Enter you job serivice: "))
if serivice>5:
    bonus=bonus+bonus*0.5
print("THE SALARY:%.2F"%bonus)