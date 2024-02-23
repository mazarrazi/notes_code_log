# 1 converting str list into int list in place  
num_list = ['9', '223', '372', '036', '854', '775', '807']  
  
for index in range(len(num_list)):  
	num_list[index] = int(num_list[index])  
	# num_list[index] = str(num_list[index]) # to change it into string  
print(num_list)  
  
# 2 converting str list into int list and appending into new list one by one  
num_list = ['9', '223', '372', '036', '854', '775', '807']  
empty_list = []  
  
for num in num_list:  
	empty_list.append(int(num))  
print(empty_list)
