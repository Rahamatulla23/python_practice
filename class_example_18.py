import math 
class Sample: 
   @staticmethod 
   def calculate(x):
      result = math.sqrt(x) 
      return result 
   
num = float(input('Enter a number:')) 
res = Sample.calculate(num) 
print('The square root of {} is {:.2f}'.format(num, res))
