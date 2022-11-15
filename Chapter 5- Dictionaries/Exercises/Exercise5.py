pets = [] #Empty list

pet = { #1st dictionary about a pet
    'Animal Type': 'Dog',
    'Name': 'Pablo',
    'Age': '1 year old',
    'Breed':'Bolonese',
    'Favorite Food': 'Chicken',
    'Gender': 'Male',
}# End of 1st dictionary
pets.append(pet) #Adding the 1st dictionary into the list

pet = { #2nd dictionary about a pet
    'Animal Type': 'Dog',
    'Name': 'Fifi',
    'Age': '2 years old',
    'Breed':'Mini Pincher',
    'Favorite Food': 'Beef',
    'Gender': 'Female',
} # End of 2nd  dictionary
pets.append(pet) #Adding the 2nd dictionary into the list

pet = {  #3rd dictionary about a pet
    'Animal Type': 'Cat',
    'Name': 'Lucky',
    'Age': '12 years old',
    'Breed':'Persian Cat',
    'Favorite Food': 'Fish',
    'Gender': 'Male',
} # End of 3rd  dictionary
pets.append(pet) #Adding the 3rd dictionary into the list


for pet in pets: #For loop for the pet(dictionary) in the pets(list).
    print("\n I have a pet named " + pet['Name'].title() + ":") #print the name of the pet, with a sentence.
    for key, value in pet.items(): #For loop to get the key and value of each pet.
        print("\t" + key + ": " + str(value)) #print the keys and value of each pet.