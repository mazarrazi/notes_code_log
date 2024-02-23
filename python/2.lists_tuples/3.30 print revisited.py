name = "Tim"  
age = 10  
  
print(name, age, "Python", 2023)  
print(name, age, "Python", 2023, sep =", ")  
  
  
# improved from 2.28  
  
# 2  
menu_list = [  
			["egg", "bacon"],  
			["egg", "sausage", "bason"],  
			["egg", "spam"],  
			["egg", "bacon", "spam"],  
			["egg", "bacon", "sausage", "spam"],  
			["spam", "bacon", "sausage", "spam"],  
			["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],  
			["spam", "egg", "spam", "spam", "bacon", "spam"]  
]  
  
for menu in menu_list:  
	for item in menu:  
		if item != "spam":  
		# print(item) # but items are printed line by line, to be improved next prg  
		print(item, end=", ") # printed next to next, but extra commas are there  
	print()  
  
# to remove those additonal commas generators and comprehension can be used  
  
  
  
# the below is using generators but not learnt yet  
  
# for menu in menu_list:  
	# items = ", ".join((item for item in menu if item != "spam"))  
	# print (items)
