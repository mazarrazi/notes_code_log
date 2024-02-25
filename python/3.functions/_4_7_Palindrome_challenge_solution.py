# challenge is to check palindrome or not for both lower & upper case letter  
  
def is_palindrome(string):  
	backward = string[::-1] # reversing the string with slice(assigns the item in reverse one by one)  
	return backward.casefold() == string.casefold() # only returns if backward == string is true  
	  
  
word = input("enter the word: ")  
if is_palindrome(word): # passing the argument & if condition in same line  
	print(f"{word} is palindrome")  
else:  
	print(f"{word} is not palindrome")  
  
  
# the above program finds palindrome or not for single word  
# but how to check for a whole sentence  
# that's the next challenge, to check palindrome or not for a sentence
