#Write a Python Program to remove duplicates in the given String.(frequenly asked question)
s = input("Enter a String: ")
ans = ''
for ch in s:#n,a,v,e,e,n
    if ch not in ans:
        ans = ans + ch

print(ans)