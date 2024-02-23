# in this program we will be choosing a song, the song should be printed alone  
  
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
	# print(songs_in_album)  
	print()  
	  
	# printing chosen song  
	INDEX_OF_SONG_TITLE = 1 # ( 0 - index no., 1 - song name) so 1  
	  
	print("Please choose your song")  
	for index, (track_number, song) in enumerate(songs_in_album):  
		print("{}: {}".format(index + 1, song))  
	print()  
	  
	song_chosen = int(input("enter the song option: "))  
	if 1 <= song_chosen <= len(songs_in_album):  
		# title = songs_in_album # print to understand  
		# title = songs_in_album[song_chosen]  
		title = songs_in_album[song_chosen][INDEX_OF_SONG_TITLE]  
	else:  
		break  
	  
	print("Playing {}".format(title))  
	print("=" * 40)  
	print()  
	print()
