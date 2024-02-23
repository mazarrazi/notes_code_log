# s[i] = x  
# i is replaced with x  
yui = ["one",  
		"two",  
		"three",  
		"four",  
		"five"  
		]  
  
print(yui)  
  
yui[3] = "eleven"  
  
print(yui)  
  
  
# s[i:j] = t , here t is iterable, so contents are replaced one by one, if list np  
# if list then np, but if its a string then it'll be replaced char by char...  
  
# with list  
yora = ["seven",  
		"eight",  
		"nine",  
		"ten",  
		"eleven"]  
print(yora)  
yora[3:] = ["twelve"]  
print(yora)  
  
# with string  
yora[4:] = "twenty" # remember not to do this if not necessary  
print(yora)  
  
# also replacing in a string not possible, because string is immutable  
# stringg = "remastered"  
# stringg[2] = "f"
