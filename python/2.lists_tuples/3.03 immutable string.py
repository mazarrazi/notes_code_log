result = "correct"  
another_result = result  
  
print(result)  
print(another_result)  
print(id(result))  
print(id(another_result))  
  
result += " guess"  
  
print(result)  
print(another_result)  
print(id(result))  
print(id(another_result))  
  
# id will be changed
