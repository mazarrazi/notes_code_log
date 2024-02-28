# how to make the same code collect all strings without printing  
# and then if quit is detected in input it'll quit and print all the collected statements  
  
# with help of chatgpt  
  
  
def banner_text(text):  
	screen_width = 80  
	if len(text) > screen_width - 4:  
		print("Text is too long")  
	if text == "*":  
		print("*" * screen_width)  
	else:  
		output_string = ("**{0}**".format(text.center(screen_width - 4)))  
		return output_string  
	  
banner_list = []  
while True:  
	input_text = input("Enter text (type 'quit' to exit): ")  
	if input_text == "quit":  
		break  
	banner_list.append(input_text)  
  
for banner in banner_list:  
	banner_output = banner_text(banner)  
	if banner_output:  
		print(banner_output)  
  
  
# To modify the code to collect all strings without printing them,  
# you can use a list to store the input strings.  
# In this code, we first create an empty list called banner_list.  
# We then modify the while loop to append each input string to the banner_list instead of printing it.  
# If the user enters "quit", the loop breaks and we move on to the next part of the code.  
#  
# After the loop, we iterate over the banner_list using a for loop. For each banner in the list,  
# we call the banner_text function with the banner as the argument and assign the result to banner_output.  
# If banner_output is not None (i.e. the text is not too long or the input was "*"), we print banner_output.  
#  
# This modified code will collect all the input strings without printing them,  
# and will only print the banners after all the input strings have been entered and  
# "quit" has been detected.
