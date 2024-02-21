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
  
z = y = x = w = another_result  
print(z)  
  
print("adding g")  
y.append("g")  
print(y)  
print(x)  
print(w)  
print(id(another_result))
