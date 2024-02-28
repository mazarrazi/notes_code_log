# from _4_13_1  
# to understand exception handling here we reduced screen width to 50  
  
  
def banner_text(text):  
	screen_width = 50  
	if len(text) > screen_width - 4:  
	#print("Text is too long")  
	raise ValueError("Text {0} is longer than specified width {1}"
	                 .format(text,screen_width))  
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
