# improvising the indexing  
albums =[  
	("Welcome to my Nightmare", "Alice Cooper", 1975,  
[  
	(1, "Welcome to my Nightmare"), (2, "Devil's Food"),  
	(3, "The Black Widow"),  
	(4, "Some Folks"),  
	(5, "Only Women Bleed"),  
]  
	),  
	("Bad Company", "Bad Company", 1974,  
[  
	(1, "Can't Get Enough"),  
	(2, "Rock Steady"),  
	(3, "Ready for Love"),  
	(4, "Don't Let Me Down"),  
	(5, "Bad Company"),  
	(6, "The Way I Choose!"),  
	(7, "Movin' On"),  
	(8, "Seagull"),  
]  
	),  
	("Nightflight", "Budgie", 1981,  
[  
	(1, "I Turned to Stone"),  
	(2, "Keeping a Rendezvous"),  
	(3, "Reaper of the Glory"),  
	(4, "She Used Me Up"),  
]  
	),  
	("More Mayhem", "Imelda May", 2011,  
[  
	(1, "Pulling the Rug"),  
	(2, "Psycho"),  
	(3, "Mayhem"),  
	(4, "Kentish Town Waltz"),  
]  
	),  
]  
  
# previously in 3.41 we used,  
# print("printing specific album")  
# album = albums[2]  
# print(album)  
# print()  
#  
# print("printing songs from that specific album")  
# songs = album[3]  
# print(songs)  
# print()  
#  
# print("printing specific song from that list of songs")  
# song = songs[1]  
# print(song)  
# print()  
#  
# print(song[1])  
  
# improvising from 3.41  
# 1  
Keeping_a_Rendezvous = albums[2][3][1][1]  
print(Keeping_a_Rendezvous)  
print()  
  
# 2  
print(albums[2][3][1][1])
