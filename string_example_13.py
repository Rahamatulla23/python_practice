#13) Write a program in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if we sent "4444444444444444", then it should return '********4444'.
s = input("Enter Credit Card Number: ").replace(' ','')

ans = (len(s)-4)*'x' +s[-4:]
print(ans)