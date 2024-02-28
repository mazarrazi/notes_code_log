# if we don't explicitly mention return for a function it'll return none  
  
# 1 function with return specified  
def multiplyy(x, y):  
	ansr = x * y  
	return ansr  
  
  
x = int(input("x : "))  
y = int(input("y : "))  
result = input(multiplyy(x, y))  
print(result)  
  
  
# 2 function without return  
def multiplyy(x, y):  
	ansr = x * y  
  
  
x = int(input("x : "))  
y = int(input("y : "))  
result = input(multiplyy(x, y))  
print(result)  
  
  
# Not All Functions return Something Useful  
# It's often useful for a function to return a value,  
# but sometimes they don't have anything to return  
# Some functions, as we've seen, return something back to the calling code.  
# You'll also write functions that perform some action, rather than calculating a value.  
# One example of that was the sort method, that we used to sort a list.  
# That was back in the section on lists.  
# The sort function didn't return anything useful, but it did perform a useful function,  
# it sorted the list.
