# there r 12 ways to create list, we'll see few  
  
# 1  
empty_list = []  
  
# 2  
even = [2, 4, 6, 8]  
odd = [1, 3, 5, 7, 9]  
  
num = even + odd  
print(num)  
  
# 3  
sorted_num = sorted(num)  
print(sorted_num)  
  
# 4  
digits1 = sorted("423159786")  
print(digits1)  
  
# 5  
digits2 = list("423159786")  
print(digits2)  
  
# 6  
more_num1 = num[:]  
print(more_num1)  
  
# 7  
more_num2 = num.copy()  
print(more_num2)  
  
  
# comparing two lists  
more_num3 = list(num)  
print(num is more_num3)  
print(num == more_num3)  
  
# The expression num is more_num3 checks if num  
# and more_num3 refer to the same object in memory,  
# while num == more_num3 checks if the two lists contain the same elements,  
# regardless of their memory address.  
  
# Since more_num3 was created using list(num),  
# it is a copy of num, but it is not the same object as num.  
# Therefore, num is more_num3 will return False,  
# while num == more_num3 will return True,  
# since both lists contain the same elements in the same order.
