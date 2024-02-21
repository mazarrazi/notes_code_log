result = ["a", "b", "c", "d", "e"]  
another_result = result  
  
print(result)  
print(another_result)  
print(id(result))  
print(id(another_result))  
  
result += ["f"]  
  
print(result)  
print(another_result)  
print(id(result))  
print(id(another_result))  
  
# id wont be changed
