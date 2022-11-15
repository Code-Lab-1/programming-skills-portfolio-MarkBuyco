#Same dictionary from Exercise 6 and 7 
student= {"Name":"Mark", "Age":"19", "Class":"Year1", "Gender":"Male", 
          "Location":"Sharjah", "Email": "markabadbuyco@gmail.com","Mobile" : "052 581 5400"}

student["Age"]= "30" #Changing the value of age in the dictionary
print(student) #Updated dictionary

student.pop("Name") #removing name(keys and values included)
print(student) #updated dictionary

student.popitem() #Removing the last(key and value) in the dictionary
print(student)