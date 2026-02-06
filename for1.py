"""adddition_Str is a string with a list of numbers separates by the + sing.write code that uses the accumulation pattern to take the sum of numbers ansd assingns it to sum_val(an integer ).(you shoulf use the .split("+")function to dplit by "+"and int()to cast to an integer)
"""
addition_str="2+5+10+20"
sum_val=0
for i in addition_str.split("+"):
    sum_val=sum_val+int(i)
print(i)  