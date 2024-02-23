from _3_43_1_data_import_for_jukebox import albums  
  
while True:  
	print("Please choose your album (invalid choice exits) ")  
	  
	# method 1  
	for index, value in enumerate(albums):  
		print("{}: {}"  
			  .format(index + 1, value))  
	print()  
	  
	# method 2  
	for index, value in enumerate(albums):  
		title, artist, year, songs = value  
		print("{}: {} {} {} {}"  
			  .format(index + 1, title, artist, year, songs))  
	print()  
	  
	# method 3  
	for index, (title, artist, year, songs) in enumerate(albums):  
		print("{}: {} {} {} {}"  
		      .format(index + 1, title, artist, year, songs))  
	print()  
	  
	break  
	  
	  
	#  this method won't work,  
	#  ValueError: not enough values to unpack (expected 5, got 2)  
	# for index, title, artist, year, songs in enumerate(albums):  
		#  print("{}: {} {} {} {}"  
			    # .format(index + 1, title, artist, year, songs))  
	# print()  
  
  
# method 2 is easiest, method 3 is preferred  
# method 1 has everything inside a tuple, methods 2 & 3 will only have the songs  
  
# program not finished yet
# in this program album, artist, songs, year all printed at same time but,  
# in our program first it should show available albums to choose,  
# after choosing a album it should show available songs to choose  
# then after choosing a song, the song should be printed alone
