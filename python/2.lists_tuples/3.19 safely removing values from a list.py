data = [4, 5, 105, 110, 120, 130, 130, 150,  
160, 170, 183, 185, 187, 188, 191, 350, 360]  
  
min_valid = 100  
max_valid = 200  
  
# 1. first process the low values in the list  
  
stop = 0  
for index, value in enumerate(data):  
	if value >= min_valid: # only no. larger than 100 are allowed  
		stop = index # index of the first largest no.  
		break  
  
# here data is deleted after the loop so no problem in index values  
print(stop)  
del data[:stop] # delete data from start of the loop until before the stop value  
print(data)
