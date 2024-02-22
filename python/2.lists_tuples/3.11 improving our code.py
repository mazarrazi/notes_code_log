listt = ["aaa", "bbb", "cc", "ddd", "eeee"]  
  
# valid_choices = [str(i) for i in range(1, len(listt) + 1)]  
valid_choices = []  
for i in range(1, len(listt) + 1):  
	valid_choices.append(str(i))  # str() is important
print(f"valid choices are \n{valid_choices}\n\n")  
current_choice = " "  
my_list = []  
  
while current_choice != "0":  
	if current_choice in valid_choices:  
		print(f"adding option {current_choice} to my list ")  
		indexx = int(current_choice) - 1   # int() is important
		chosen_option = listt[indexx]  
		my_list.append(chosen_option)  
	else:  
		print("add choices from this list")  
		for num, charc in enumerate(listt):  
			print(f"{num + 1}: {charc}") 
			 
	current_choice = input("enter option ")  
print(my_list)  
  
# run this code in debugger with breakpoints in line 14 15 16
