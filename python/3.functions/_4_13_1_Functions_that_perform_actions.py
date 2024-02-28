#  1  
def banner_text(text):  
	screen_width = 80  
	if len(text) > screen_width - 4:  
		print("Text is too long")  
	if text == "*":  
		print("*" * screen_width)  
	else:  
		output_string = ("**{0}**".format(text.center(screen_width - 4)))             
		# screen_width - 4 because 4 *  
		print(output_string)  
	  
  
banner_text("*")  
banner_text("Always look on the bright side of life...")  
banner_text("If life seems jolly rotten, ")  
banner_text("There's something you've forgotten!")  
banner_text("And that's to laugh and smile and dance and sing,")  
banner_text(" ")  
banner_text("When you're feeling in the dumps,")  
banner_text("Don't be silly chumps,")  
banner_text("*")  
  
  
  
#  2 input at runtime  
def banner_text(text):  
	screen_width = 80  
	if len(text) > screen_width - 4:  
		print("Text is too long")  
	if text == "*":  
		print("*" * screen_width)  
	else:  
		output_string = ("**{0}**".format(text.center(screen_width - 4))) 
		# screen_width - 4 because 4 *  
		#print(output_string)  
		return output_string  
  
input_text = input("enter text: ")  
while input_text != "quit":  
	xox = banner_text(input_text)  
	print(xox)  
  
#  this is infinite loop, i want it to ask for input after each time statement is printed  
#  so updated it further  
  
  
  
#  3 input at runtime  
def banner_text(text):  
	screen_width = 80  
	if len(text) > screen_width - 4:  
		print("Text is too long")  
	if text == "*":  
		print("*" * screen_width)  
	else:  
		output_string = ("**{0}**".format(text.center(screen_width - 4)))  
		return output_string  
	  
	while True:  
		input_text = input("Enter text (type 'quit' to exit): ")  
		if input_text == "quit":  
			break  
		banner = banner_text(input_text)  
		if banner:  
			print(banner)  
        # input("Press Enter to continue...")
