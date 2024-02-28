# previously we were passing 66 as argument in every function call  
# here instead of passing 66 each time we declare the argument along with the parameter name just once  
def banner_text(text, screen_width=66):  
	if len(text) > screen_width - 4:  
		#print("Text is too long")  
		raise ValueError("Text {0} is longer than specified width {1}"
		                 .format(text, screen_width))  
	if text == "*":  
		print("*" * screen_width)  
	else:  
		output_string = ("**{0}**"
		         .format(text.center(screen_width - 4))) # screen_width - 4 because 4 *  
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
  
  
# here we're passing the arguments for few function for understanding  
def banner_text(text, screen_width=66):  
	if len(text) > screen_width - 4:  
		#print("Text is too long")  
		raise ValueError("Text {0} is longer than specified width {1}"
		                 .format(text, screen_width))  
	if text == "*":  
		print("*" * screen_width)  
	else:  
		output_string = ("**{0}**"
		        .format(text.center(screen_width - 4))) # screen_width - 4 because 4 *  
		print(output_string)  
		  
	  
banner_text("*")  
banner_text("Always look on the bright side of life...")  
banner_text("If life seems jolly rotten, ")  
banner_text("There's something you've forgotten!", 80)  
banner_text("And that's to laugh and smile and dance and sing,")  
banner_text(" ")  
banner_text("When you're feeling in the dumps,", 80)  
banner_text("Don't be silly chumps,")  
banner_text("*")
