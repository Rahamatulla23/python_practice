def avg(list): 
   tot=0 
   for x in list: #1,2,3,4,5
      tot+=x 
   avg = tot/len(list) 
   return tot, avg 

try: 
   t,a = avg([1,2,3,4,5]) 

   print('Total= {}, Average= {}'.format(t,a)) 
except TypeError: 
   print('Type Error, please provide numbers.') 
except ZeroDivisionError: 
   print('ZeroDivisionError, please do not give empty list.')
