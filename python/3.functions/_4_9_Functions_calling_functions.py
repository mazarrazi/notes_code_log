# here one function is calling another function  
  
# c. this function determines whether the processed string is a palindrome and return  
def is_palindrome(string): # 4  
	backward = string[::-1]  
	return backward == string # 5  
  
# b. this function removes any non-alphanumeric characters  
def palindrome_sentence(sentence): # 2  
	word = "" # empty string  
	for char in sentence:  
		if char.isalnum():  
			word += char  
	print(word)  
	return is_palindrome(word) # 3  
  
# a.  
input_word = input("enter the word: ")  
if palindrome_sentence(input_word): # 1  
	print(f"{input_word} is palindrome")  
else:  
	print(f"{input_word} is not palindrome")  
  
# here at 1 func is called, which takes program flow to 2  
# inside that function at 3 another func is called, which takes the flow to 4  
# the value is not returned from step 5 to step 4 to step 3 and so on.  
# Instead, the value is returned directly from step 5 to step 2 to main program  
  
  
# The program starts by calling the palindrome_sentence function with the user input word or sentence.  
# The palindrome_sentence function processes the input by removing any non-alphanumeric characters and  
# returns the result of the is_palindrome function with this processed string as its argument.  
# The is_palindrome function determines whether the processed string is a palindrome  
# and returns True or False.  
# The result of is_palindrome is returned to the palindrome_sentence function.  
# The palindrome_sentence function returns the result of is_palindrome to the main program.  
# Finally, the main program uses an if statement to print a message indicating  
# whether the input is a palindrome or not.
