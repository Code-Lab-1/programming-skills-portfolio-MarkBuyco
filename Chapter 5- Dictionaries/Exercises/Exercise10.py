#Dictionary containing my favorite songs
songs = {
    'ILYSB': 'LANY',
    'Only Exception': 'Paramore',
    'Iris': 'Goo Goo Dolls',
    'Hearbreat Anniversary': 'Giveon',
    'The Scientist': 'Coldplay',
        } #End of dictionary containing 5 of my favorite songs and artist

for song,artist in songs.items(): #For loop to get keys and values in the dictionary.
    print(song.title() + " was sunged by " + artist.title() + ".") #Print data with a sentence.

print("\n These are the songs included in the dictionary:") #print heading
for song in songs.keys(): # For loop to get the keys in the dictionary.
    print("- " + song.title()) #print the keys, which is the songs.

print("\nThese are the artists included in the dictionary:") #print heading
for artist in songs.values(): # For loop to get the valued in the dictionary.
    print("- " + artist.title()) #print the values, which is the artist.