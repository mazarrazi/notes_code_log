
def is_palindrome(string):  
	backward = string[::-1] # reversing the string with slice(assigns the item in reverse one by one)  
	return backward == string # only returns if backward == string is true  
  
  
word = input("enter the word: ")  
if is_palindrome(word): # passing the argument & if condition in same line  
	print(f"{word} is palindrome")  
else:  
	print(f"{word} is not palindrome")
