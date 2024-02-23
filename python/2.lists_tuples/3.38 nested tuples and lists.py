# we need a list of tuples  
  
# these are individual tuples  
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975  
bad = "Bad Company", "Bad Company", 1974  
budgie = "Night flight", "Budgie", 1981  
imelda = "More Mayhem", "Emilda May", 2011  
metallica = "Ride the Lightning", "Metallica", 1984  
print(welcome)  
print()  
  
# this is a list containing 15 items  
albums = ["Welcome to my Nightmare", "Alice Cooper", 1975,  
		  "Bad Company", "Bad Company", 1974,  
		  "Night flight", "Budgie", 1981,  
		  "More Mayhem", "Emilda May", 2011,  
	      "Ride the Lightning", "Metallica", 1984,  
]  
print(albums)  
print(len(albums))  
print()  
  
# by adding parenthesis it'll be a list of 5 tuples  
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),  
		  ("Bad Company", "Bad Company", 1974),  
		  ("Night flight", "Budgie", 1981),  
		  ("More Mayhem", "Emilda May", 2011),   
		  ("Ride the Lightning", "Metallica", 1984),  
]  
print(albums)  
print()  
  
# printing album one by one  
for album in albums:  
	print("album:{0} artist:{1} year:{2}\n"  
		  .format(album[0], album[1], album[2]))  
	  
  
# challenge: improvise the code 
# for album in albums:  
# print("album:{0} artist:{1} year:{2}\n"  
# .format(album_name, artist, year))
