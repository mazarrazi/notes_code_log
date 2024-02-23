drot = "A b C d E f"  
  
a = sorted(drot)  
print(a)  
  
# b = sorted(key=str.casefold)  
# print(b)  
# the above won't work  
  
b = sorted(drot, key=str.casefold)  
print(b)  
  
c = sorted("a B c D e F",  
key=str.casefold)  
print(c)  
  
  
# drot.sort(key=str.casefold)  
# print(drot)  
# the above won't work because,  
# drot is a string but not a list and  
# sort() method will work only for list  
# you can convert drot to a list using the list() function  
  
drot_list = list(drot)  
drot_list.sort(key=str.casefold)  
print(drot_list)
