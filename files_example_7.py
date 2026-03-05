f = open('naveen.txt', 'a+') 
print('Enter text to append:') 
while True: 
   str = input() 
   if(str == 'e'): 
     break
   
   f.write(str+"\n") 

f.seek(4,0) 
#read strings from the file 
print('The file contents are:') 
str = f.read() 
print(str) 
#closing the file 
f.close()
