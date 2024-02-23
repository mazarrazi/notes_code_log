# in previous program album, artist, songs, year all printed at same time but,  
# in our program first it should show available albums to choose,(previous prg)  
# after choosing a album it should show available songs to choose, (this prg)  
# then after choosing a song, the song should be printed alone, (next prg)  
  
# in this the program will show songs in chosen album  
  
  
from _3_43_1_data_import_for_jukebox import albums  
  
while True:  
	print("Please choose your album (invalid choice exits) ")  
	  
	# printing available albums  
	for index, (title, artist, year, songs) in enumerate(albums):  
		print("{}: {}"  
		      .format(index + 1, title))  
	print()  
	# break  
	  
	# asking for album choice  
	# album_choice = int(input(f"enter option from 1 to {len(albums) + 1}: "))  
	album_choice = int(input("enter option: "))  
	  
	# print songs from the chosen album  
	if 1 <= album_choice <= len(albums):  
		songs_in_album = albums[album_choice - 1][3]  
		# albums[index of album in list] [index 3 is where songs list is present]  
	else:  
		break  
	print(songs_in_album)  
	print()  
  
# code not completed yet, after printing songs list,  
# we should be choosing a song, the song should be printed alone,  
  
  
# using a constant in same code  
  
  
from _3_43_1_data_import_for_jukebox import albums  
  
while True:  
	print("Please choose your album (invalid choice exits) ")  
	  
	# printing available albums  
	for index, (title, artist, year, songs) in enumerate(albums):  
		print("{}: {}"  
		     .format(index + 1, title))  
	print()  
	# break  
	  
	# asking for album choice  
	# album_choice = int(input(f"enter option from 1 to {len(albums) + 1}: "))  
	album_choice = int(input("enter option: "))  
	  
	INDEX_OF_SONGS_LIST = 3 # CONSTANT should be capital  
	# if we see capital variables then it should not be altered  
	  
	# print songs from the chosen album  
	if 1 <= album_choice <= len(albums):  
		songs_in_album = albums[album_choice - 1][INDEX_OF_SONGS_LIST]  
		# albums[index of album in list] [index 3 is where songs list is present]  
	else:  
		break  
	print(songs_in_album)  
	print()
