#8) Write a Python program to find the maximum occurring character in a given string.(frequenly asked question)
s = input("Enter a String: ").lower()
max_value = 0

for ch in s:# r,a,i,n,y, d,a,y,s, a,h,e,a,d
    if s.count(ch)>max_value:
        max_char = ch
        max_value = s.count(ch)

print(max_char)