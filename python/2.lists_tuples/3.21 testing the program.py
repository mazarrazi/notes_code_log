# code from 3.20, test case from 3.21.0  
  
# 1. outlying values at the low and high ends  
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,  
# 160, 170, 183, 185, 187, 188, 191, 350, 360]  
  
# 2. outlying values at the low-end only  
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,  
# 160, 170, 183, 185, 187, 188, 191]  
  
# 3. outlying values at the high-end only  
# data = [104, 105, 110, 120, 130, 130, 150,  
# 160, 170, 183, 185, 187, 188, 191, 350, 360]  
  
# 4. no outlying values  
# data = [104, 105, 110, 120, 130, 130, 150,  
# 160, 170, 183, 185, 187, 188, 191]  
  
# 5. only outlying values (no valid ones)  
data = [1041, 1051, 1101, 1110, 1120, 1130, 1130, 1150,  
		1161, 1177, 1183, 1185, 1187, 1188, 1191, 1350, 1360]  
  
# 6. an empty data set  
# data = []  
  
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
		break  
  
print(start) # index no.  
del data[start:]  
print(data)
