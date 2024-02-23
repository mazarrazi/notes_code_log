# iterating forwards messes up index, iterating backwards won't  
data = [104, 101, 4, 105, 308, 103, 5,  
107, 100, 306, 106, 102, 108]  
  
min_valid = 100  
max_valid = 200  
  
# method 1 of printing list in reverse  
# for index in range(len(data) - 1, -1, -1):  
#      print(index, data) # to understand indexing  
  
  
for index in range(len(data) - 1, -1, -1):  
	print(index, data)  
	if(data[index] < min_valid) or data[index] > max_valid:  
		del data[index]  
		print(f"{index} {data} after removing")  
print(data)  
  
  
# removing items in a list by iterating backwards in a loop  
# the problem with forward iteration is,  
# when we remove index 2 from [1, 2, 3, 4, 5] 3 is removed and 4 comes to index 2  
#                       index [0, 1, 2, 3, 4] iterates this way -->  
# index 2 is already checked by for loop so it'll move to next index without checking it  
# no checking properly creates errors  
  
# but iterating backwards won't create this index problem  
# when we remove index 2 from [1, 2, 3, 4, 5, 6] 4 is removed and 5 comes to index 2,  
#                       index [5, 4, 3, 2, 1, 0] <-- iterates this way  
# but we've already checked value 5 since we're iterating backwards, so no check needed  
# loop will now check index 3 value 3,  
# if value 3 is removed then value 5 comes to index 3  
# TL;DR: iterating forwards messes up index, iterating backwards won't
