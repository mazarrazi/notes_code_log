choice = " "  # the space is important without that its infinity loop
  
while True:  
	if choice == "0":  
		break  
	elif choice in "12345":  
		print(f"you choose {choice}.")
		break  
	else:  
		print("available options")  
		print("1.\t solve python")  
		print("2.\t solve C")  
		print("3.\t go do art")  
		print("4.\t tinker hardware")  
		print("5.\t simulate particles")  
		print("0.\t exit")  
	choice = input("enter option ")
