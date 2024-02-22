current_option = " "  # empty space is important
listt = [ ] # initializing empty list  
  
while current_option != "0":  
	if current_option in "12345":
		print(f"adding option {current_option} in my list")  
		if current_option == "1":  
			listt.append("a")  
		elif current_option == "2":  
			listt.append("b")  
		elif current_option == "3":  
			listt.append("c")  
		elif current_option == "4":  
			listt.append("d")  
		elif current_option == "5":  
			listt.append("e")  
	else:  
		print("available option")  
		print("1.\t a")  
		print("2.\t b")  
		print("3.\t c")  
		print("4.\t d")  
		print("5.\t e")  
		print("0.\t exit")  
	current_option = input("enter option ")  
  
print(listt)
