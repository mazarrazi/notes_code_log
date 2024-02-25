# update from _4_10  
# if anything other than numeric is given as input then it'll print warning  
  
import random  
  
def get_integer(prompt):  
	while True:  
		temp = input(f"enter input{prompt} ")  
		if temp.isnumeric():  
			return int(temp)  
		#else:  
		print(f"{temp} is not a number")  
	  
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
