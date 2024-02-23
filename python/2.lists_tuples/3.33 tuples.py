# tuple uses () whereas list uses [].  
# tuple immutable & requires lesser memory, list mutable.  
# tuple is ordered, its a sequence. In python being ordered is requirement for sequence  
  
t = ("a", "b", "c")  
w = "a", "b", "c"  
print(t)  
print(w)  
# w is printed with () by default, but still using parenthesis is preferred  
  
  
name = "Tim"  
age = 10  
print(name, age, "Python", 2021)  
print((name, age, "Python", 2021))  
# here if tuple is needed using () inside print() is necessary  
# () is required if tuple is passed as literal argument inside a function
