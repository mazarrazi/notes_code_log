listt = ["a", "b", "c", "d", "e"]  
current_choice = " "  
my_list = []  
  
# valid_choices = [str(i) for i in range(1, len(listt) + 1)]  
valid_choices = []  
for i in range(1, len(listt) + 1):  
valid_choices.append(str(i))  
print(f"valid choices are \n{valid_choices}\n\n")  
  
while current_choice != "0":  
	if current_choice in valid_choices:  
		if current_choice in my_list:  
			print(f"removing {current_choice} from {my_list}")  
			my_list.remove(current_choice)  
		else:  
			print(f"adding {current_choice} into {my_list}")  
			my_list.append(current_choice)  
		print(f"list now contains\n{my_list}\n")  
	else:  
		print("add choices from this list")  
		for num, charc in enumerate(listt):  
			print(f"{num + 1}: {charc}")  
  
current_choice = input("enter option ")  
print(my_list)
