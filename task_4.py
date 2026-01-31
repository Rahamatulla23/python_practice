"""Grade Calculator
Input marks (0–100)
Output:
90–100 → A
75–89 → B
50–74 → C
<50 → Fail"""
marks=int(input("Enter marks:"))
if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks>=75  and marks<=89:
    print("Grade B")
elif marks>=50 and marks<=74:
     print("Grade c")
else:
     print("Fail")

