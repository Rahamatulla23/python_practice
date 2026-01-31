"""Multiplication Table
Input a number
Print table up to 10"""
table=int(input("Enter a number you want table:"))
for i in range(1,11):
        print(f"{table}*{i}={i*table}")