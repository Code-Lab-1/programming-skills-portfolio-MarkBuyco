#Dictionary containing major rivers
major_river = {
    'Amazon river': 'South America',
    'Ob river': 'Russia',
    'Niger river': 'Africa',
        } #End of dictionary containing 3 major rivers plus the country it belongs. 

for river,place in major_river.items(): #For loop to get keys and values in the dictionary.
    print("The " + river.title() + " In in the country of " + place.title() + ".") #Print data with a sentence.

print("\n These are the rivers included in the dictionary:") #print heading
for river in major_river.keys(): # For loop to get the keys in the dictionary.
    print("- " + river.title()) #print the keys, which is the rivers.

print("\nThese are the countries or place included in the dictionary:") #print heading
for place in major_river.values(): # For loop to get the valued in the dictionary.
    print("- " + place.title()) #print the values, which is the place/country.