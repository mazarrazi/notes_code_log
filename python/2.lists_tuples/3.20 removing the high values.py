data = [4, 5, 105, 110, 120, 130, 130, 150,  
160, 170, 183, 185, 187, 188, 191, 350, 360]  
  
print(data)  
min_valid = 100  
max_valid = 200  
  
# 1. first process the low values in the list  
  
stop = 0  
for index, value in enumerate(data):  
	if value >= min_valid: # only no. larger than 100 are allowed  
		stop = index # index of the first largest no.  
		break  
  
# here data is deleted after the loop so no problem in index values  
print(stop) # index no.  
del data[:stop] # delete data from start of the loop until before the stop value  
print(data)  
  
# 2. process the high values in the list  
start = 0  
for index in range(len(data) - 1, -1, -1):  
	if data[index] <= max_valid:  
		start = index + 1  
		# index + 1 because of slicing/deleting,  
		# [start : stop -1] this is how slicing occurs  
		# del[0 : 2) then 0,1 are deleted  
		# if we have, del data[index : stop -1] then index will also get deleted,  
		# so instead we will have [index +1 : stop -1]  
		# in this program stop -1 won't be needed, because  
		# we implement in algo itself, check # 1 for more details  
		break  
	  
print(start) # index no.  
del data[start:]  
print(data)
