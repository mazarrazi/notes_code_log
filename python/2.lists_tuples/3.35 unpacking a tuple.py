# unpacking a tuple is important  
  
# 1  
data = 1, 34, 78  
x, y, z = data # this is  
print(x)  
print(y)  
print(z)  
  
# 1 is as same as 2  
  
# 2  
data_list = [27, 63, 89]  
p, q, r = data_list # this, here were unpacking the list into three variables  
print(p)  
print(q)  
print(r)  
# any sequence type can be unpacked  
  
# 3  
data_list = [27, 63, 89]  
data_list.append(34)  
print(data_list)  
  
# 4  
data_list = [27, 63, 89]  
data_list.append(56) # error  
x, y, z = data_list  
print(data_list)  
  
# in 3 we appending value to list  
# in 4 we are unpacking list into three variables,  
# but also appending another variable with existing list  
# the additional value causes error during unpacking
