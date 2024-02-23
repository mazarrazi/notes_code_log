# The join() method takes all items in an iterable and joins them into one string.  
# A string must be specified as the separator.  
# the join method iterates over the list for us  
  
numbers = ["one",  
		   "two",  
		   "three",  
		   "four",  
		   "five",  
	       "six",  
		   "se7en"  
		   ]  
  
for humber in numbers:  
	print(numbers)  
  
# method 1  
separator = " | "  
output = separator.join(numbers)  
print(output)  
  
# method 2  
print((", ".join(numbers)))
