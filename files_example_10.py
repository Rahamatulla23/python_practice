f1 = open('cat.jpeg', 'rb') 
f2 = open('new.jpg', 'wb') 

f2.write(f1.read() ) 

f1.close()
f2.close()
