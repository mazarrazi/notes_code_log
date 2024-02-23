data = [4, 5, 104, 105, 110, 120, 130, 130, 150,  
160, 170, 183, 185, 187, 188, 191, 350, 360]  
# from the list we want to delete values below 100 and above 200  
  
# 1. trying to delete with index value  
del data[0:2]  
print(data)  
del data[16:]  
print(data)  
# after deleting the first two numbers the index value of list changed so...  
# so the last two numbers won't be deleted  
del data[14:] # manually correcting index value  
print(data)  
  
# re-initializing for next type  
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,  
160, 170, 183, 185, 187, 188, 191, 350, 360]  
  
# 2. trying to delete with for loop  
for index, value in enumerate(data):  
	if(value <= 100) or (value > 200):  
		del data[index]  
print(data)  
# again index problem, but this is a different one  
# check this part in debugger with breakpoint  
# the problem is, if 350(index 18) is deleted then 360 will come to its place  
# 360 will move from index 19 to 18, but for loop has already went past index 18  
# so now 360 will be ignored from being deleted  
  
# re-initializing for next type  
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,  
160, 170, 183, 185, 187, 188, 191, 350, 360]  
  
# 3. we try the above with C's index-- alternate  
for index, value in enumerate(data):  
	if(value <= 100) or (value > 200):  
		del data[index]  
		index -= 1  
print(data)  
# the index -= 1 is alternate of index -- from C  
# python for loop won't work as same as C or Java for loop  
# here the index will reset everytime line 35 is executed(for loop)  
# so you can't mess with the flow of a for loop in python  
# by manipulating the loop control variable
