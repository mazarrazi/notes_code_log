pangram = "The quick brown fox jumps over the lazy dog"  
  
letters = sorted(pangram)  
print(letters)  
  
num1 = [2.3, 4.5, 8.7, 9.2, 1.6]  
sorted_num1 = sorted(num1)  
print("\nafter sorted() function")  
print(f"num1 = {num1}")  
print(f"sorted_num1 = {sorted_num1}\n\n")  
# num won't be sorted only sorted_num1 will be sorted  
  
num2 = [1.2, 5.4, 9.6, 3.8, 7.0]  
sorted_num2 = num2.sort()  
print("after sort() method with assigning")  
print(f"sorted_num2 = {sorted_num2}\n")  
# sort() method doesn't have return value so cannot be assigned  
num2.sort()  
print("after sort() method without assigning")  
print(f"num2= {num2}")  
  
# if you want to change a variable name throughout the program then,  
# select the name i.e. num1 right click refactor and change the name
