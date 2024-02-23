# challenge soln  
# improvising the code  
  
# 1  
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),  
		  ("Bad Company", "Bad Company", 1974),  
		  ("Night flight", "Budgie", 1981),  
		  ("More Mayhem", "Emilda May", 2011),  
		  ("Ride the Lightning", "Metallica", 1984),  
]  
  
for album in albums:  
	name, artist, year = album  
	print("album:{0} artist:{1} year:{2}\n"  
		  .format(name, artist, year))  
  
print("```````````````````````````````````````````````````````````````")  
  
# 2  
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),  
		  ("Bad Company", "Bad Company", 1974),  
		  ("Night flight", "Budgie", 1981),  
		  ("More Mayhem", "Emilda May", 2011),  
		  ("Ride the Lightning", "Metallica", 1984),  
]  
  
for name, artist, year in albums:  
	print("album:{0} artist:{1} year:{2}\n"  
		  .format(name, artist, year))  
  
  
# in 1 for each iteration we albums one by one into album,  
# then unpacked from album into variables.  
  
# in 2 we directly unpacked from albums into variables for each iteration  
  
# 1 is improvised from precious prg and 2 is improvised from 1
