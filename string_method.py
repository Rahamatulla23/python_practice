'''
All String Method 
1.index("it repersent the index of the elemet to string if element not in the string then  it going through the value error  ")
2.rindex("it repersent the index  form right side")
3.find("it repersent the index of a element and if element not in the string then  it going through the -1")
4.rfind("it repersent the index  form right side")
5.lower()->it change the full string to lower case form upper 
6.upper()->it change the full string to upper case form lower
7.title()->Capitalizes the first character, all others are converted to lowercase.
8.capitalize()->Capitalizes the first character of each word, all others are converted to lowercase.
9.swapcase()->it going to change upper case letters to lower and lower case to upper case
10.split()->it going cut the string using dlimiter,if we don't pass any dlimiter then it defaultly task space as delimirt
11.join()->the method is used to join the  string
12.startsswith()->it check the string is that starting with (delimeter) if it is then it display TRUE if not then FALSE
13.endswith()->it check the string is that ending with (delimeter) if it is then it display TRUE if not then FALSE
14.count()->it check the (delimeter) count is it is persent then it display the count if it is not then it gong to diaplay the 0
15.replace()->it gong to replace the valuse depending on the(delimeter)
16.isalnum()->returns True if a string contains only letters and/or numbers.
It returns False if the string contains any symbols, punctuation, or spaces An empty string also returns False
17.isalpha()->returns True if a string contains only letters.It returns False if the string contains any numbers, spaces, symbols, or punctuation.
An empty string also returns False
18.isdigit()-> returns True if a string contains only characters that can be represented as digits. This includes decimal digits (0-9) and also digits in other number systems, such as Unicode digits.
It returns False if the string contains any letters, spaces, symbols, or punctuation.
An empty string also returns False
19.isupper()->returns True if all letters in the string are uppercase.It ignores numbers, symbols, and spaces when making its determination.It returns False if the string contains at least one lowercase letter.It also returns False if the string contains no cased characters
20.islower()->returns True if all letters in the string are lowercase.It ignores numbers, symbols, and spaces when making its determination.It returns False if the string contains at least one uppercase letter.It also returns False if the string contains no cased characters
21.istitle()->determines if a string is title cased by checking the case of each word's characters. A "word" is a sequence of letters separated by non-letter characters like spaces, numbers, or symbols.It returns True only if:The first letter of every word is uppercase.All other letters within each word are lowercase.It returns False if:Any word starts with a lowercase letter.Any word contains an uppercase letter
after the first character.The string contains no cased characters.
22.isspace()->returns True if a string contains nothing but characters like: Space (' ')Tab ('\t')Newline ('\n')Carriage Return ('\r')It returns False if the string contains any visible characters (letters, numbers, symbols).An empty string also returns False.
23.concatenation->it going join two string using("+")
24.id()->it display address of  particular variable
 
'''
s = " This Is a Sample String "
print(s.split(" "))#it going to splite string with spaces
print(s.startswith("This"))#it going to return boolen value
print(s.endswith("string"))#it also return boolen value
print(s.strip())#it going to remove leading and trailing spaces
print(s.rstrip())#it going to remove leading  spcae
print(s.lstrip())#it going to remove trailing space
print(s.replace('String','of python'))#it going to replace the string
print(s.isalpha())#it check is alphabets if it is it returns true
print(s.islower())#it check is string is in lower case
print(s.isupper())#it check is string is in supper case
print(id(s))#it return adderess of string
print(s.istitle())#it checks the string is in title case 
print(s.isdigit())#it checks the string is digite 
print(s.find('I'))#it check the how many time is delimiter is repeated
print(s.index('Is'))# it return index value of delimiter