#3) Write a Python program to remove the characters which have odd index values of a given string.

s = input("Enter a String: ")
ans = ''
for ch in s[::2]:#C,a,l,e,K,i, ,s,n, ,o,e
    ans = ans + ch
print(ans)

for i in range(0, len(s),2):
    print(s[i],end='')