"""
11) Write a Python Program to REVERSE internal content of each word?
    Input: Python is Simple
    Output: nohtyP si elpmiS
"""
s = input("Enter a String: ")
ans = ''

for word in s.split():#'Python', 'is', 'Simple'
    ans = ans + word[::-1] + " "
print(ans.strip())