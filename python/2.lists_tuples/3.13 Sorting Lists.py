even = [2, 4, 6, 8]  
odd = [1, 3, 5, 7, 9]  
  
even.extend(odd) # adding odd data to even  
even.sort() # sorting the whole data  
print(f"even: {even}")  
  
another_even = even  
print(f"another_even: {another_even}")  
  
# reverse sort  
even.sort(reverse=True)  
print(even)  
print(another_even) # change in even changes another_even too
