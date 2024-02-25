
def palindrome_sentence(sentence):  
	word = "" # empty string  
	for char in sentence:  
		if char.isalnum():  
			word += char # storing char by char in empty string if it is alphabet or numeric only  
		  
	return word[::-1] == word  
  
  
input_word = input("enter the word: ")  
if palindrome_sentence(input_word): # passing the argument & if condition in same line  
	print(f"{input_word} is palindrome")  
else:  
	print(f"{input_word} is not palindrome")
