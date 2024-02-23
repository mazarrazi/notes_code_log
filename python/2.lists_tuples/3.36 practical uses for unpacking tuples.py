# 1  
for t in enumerate("abcdef"):  
	print(t)  
print()  
  
# 2  
for t in enumerate("abcdef"):  
	index, character = t  
	print(index, character)  
print()  
  
# 3  
for index, character in enumerate("abcdef"):  
	print(index, character)  
print()  
  
# 1 - tuple unpacked into t by enumerate()  
# 2 - tuple is stored in t, in each loop, then t is unpacked into index & character  
# 3 - every loop tuple is directly unpacked into index, character  
  
# 3 is the easier version of 2
