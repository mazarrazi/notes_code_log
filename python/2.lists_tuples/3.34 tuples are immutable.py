welcome = "Welcome to my Nightmare", "Alice Cooper", 1975  
bad = "Bad Company", "Bad Company", 1974  
budgie = "Night flight", "Budgie", 1981  
imelda = "More Mayhem", "Emilda May", 2011  
metallica = "Ride the Lightning", "Metallica", 1984  
  
print(metallica)  
print(metallica[0]) # even for tuple [] is used for index operations  
print(metallica[1])  
print(metallica [2])  
  
# changing values of tuple not possible  
# (metallica[0]) = "Master of Puppets" # error  
  
# to change a value in a tuple we can try alternate way,  
# convert tuple into list using list() assign to another variable  
# change the value in the list  
# convert list into tuple using tuple()  
  
metallica2 = list(metallica)  
print(metallica2)  
  
metallica2[0] = "Master of Puppets"  
print(metallica2)  
  
metallica2 = tuple(metallica2)  
print(metallica2)
