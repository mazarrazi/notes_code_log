# challenge is to add another parameter to the function  
# we will consider screen width as that parameter  
  
def banner_text(text, screen_width):  
	if len(text) > screen_width - 4:  
		#print("Text is too long", 66)  
		raise ValueError("Text {0} is longer than specified width {1}"
		                 .format(text, screen_width))  
	if text == "*":  
		print("*" * screen_width)  
	else:  
		output_string = ("**{0}**"
	            .format(text.center(screen_width - 4))) # screen_width - 4 because 4 *  
		print(output_string)  
  
  
banner_text("*", 66)  
banner_text("Always look on the bright side of life...", 66)  
banner_text("If life seems jolly rotten, ", 66)  
banner_text("There's something you've forgotten!", 66)  
banner_text("And that's to laugh and smile and dance and sing,", 66)  
banner_text(" ", 66)  
banner_text("When you're feeling in the dumps,", 66)  
banner_text("Don't be silly chumps,", 66)  
banner_text("*", 66)
