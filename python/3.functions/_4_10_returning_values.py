# update from 2.23  
# in the update only numeric input is allowed, if its not numeric the prompt asks for input again  
  
import random  
  
def get_integer(prompt):  
	while True:  
	temp = input(f"enter input{prompt} ")  
	if temp.isnumeric(): # checks if temp is numeric  
		return int(temp) # returns temp in int type  
		# note return acts as a break, so flow breaks away from the while loop here & value is returned  
  
  
highest = int(input("enter highest value \n"))  
guess = 0  
answer = random.randint(1, highest)  
# print(answer)  
  
while guess != answer:  
  
	guess = get_integer(": ")  
	if guess == 0:  
		break  
	if guess == answer:  
		print("correct1")  
		break  
	else:  
		if guess < answer:  
			print("guess higher\n")  
		else:  
			print("guess lower\n")  
		  
  
# in execution if alphabets or anything other than numerics are given it asks for input again  
  
# challenge,  
# Modify the get_integer function so that it prints a message, if the user enters an invalid number.
