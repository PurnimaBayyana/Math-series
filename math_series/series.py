# Define the Fibonacci function in recursive method
def fibonacci(n):
 '''Takes in a number n ,returns the Fibanacci element '''  
 if n < 0: 
  print("Incorrect input") 
# First Fibonacci number is 0 
 elif n==0: 
    return 0
# Second Fibonacci number is 1 
 elif n==1: 
   return 1
 else: 
   return fibonacci(n-1)+fibonacci(n-2) 
# Driver function 
print(fibonacci.__doc__)
print(fibonacci(7))


## ------------------------------------------------------------------------------

# Define the Lukas function in recursive method

def lukas(n):
 '''Takes in a number n ,returns the Lukas element '''  
 if n < 0: 
  print("Incorrect input") 
# First Fibonacci number is 0 
 elif n==0: 
    return 2
# Second Fibonacci number is 1 
 elif n==1: 
   return 1
 else: 
   return lukas(n-1)+lukas(n-2) 
# Driver function 
print(lukas.__doc__)
print(lukas(7))

## ------------------------------------------------------------------------------
# Define third function sum_series to print both fibonacci or lukas based on input

def sum_series(y,z=0,w=0):
 print('-----------------------------------------')
 print('Printing the values of Sum series function:')
 if z ==2 and w ==1:
  '''Takes in a mandatory parameter,returns the Fibanacci element ''' 
  print('The element' , y, 'From Lukas function is:') 
  return lukas(y)
 elif z==0 and w==0: 
  '''Takes in mandatory and optional parameters ,returns the Lukas element ''' 
  print('The element' , y, 'From Fabinacci function is:') 
  return fibonacci(y)
 else:
   print('Incorrect input')



    




