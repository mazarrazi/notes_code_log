data = [104, 101, 4, 105, 308, 103, 5,  
107, 100, 306, 106, 102, 108]  
  
print(data)  
min_valid = 100  
max_valid = 200  
  
# to index forward  
forward_index = len(data) - 1 # because reversed function indexes backwards  
  
print("\n")  
  
for index, value in enumerate(reversed(data)):  
	if value < min_valid or (value > max_valid):  
		print(forward_index - index, data)  
		# (forward_index - index) prints index in reverse  
		del data[forward_index - index]  
print(data)  
  
  
  
print("\nfor understanding")  
  
# for understanding  
  
# default reversed function  
for index, value in enumerate(reversed(data)):  
	print(index, value)  
  
print("\n")  
  
# method 2 of printing list in reverse  
# reversing the index value of reversed function to index forwards instead of backwards  
for index, value in enumerate(reversed(data)):  
	print(forward_index - index, value) 
	# (forward_index - index) prints index in reverse
