current_option = " "  
listt = ["a", "b", "c", "d", "e"]  
my_list = []  
  
while current_option != "0":  
	if current_option in "12345":  
		print(f"adding option {current_option} in my list")  
		if current_option == "1":  
			my_list.append("a")  
		elif current_option == "2":  
			my_list.append("b")  
		elif current_option == "3":  
			my_list.append("c")  
		elif current_option == "4":  
			my_list.append("d")  
		elif current_option == "5":  
			my_list.append("e")  
	else:  
		for num, charc in enumerate(listt):  
			print(f"{num + 1}: {charc}")  # num + 1 because index starts at 0 
	  
	current_option = input("enter option ")  
  
print(my_list)  
  
# example of how enumerate func works  
# for index, character in enumerate("abcdef"):  
# print(f"{index}. {character}")
