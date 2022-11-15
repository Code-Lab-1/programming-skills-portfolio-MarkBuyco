#Who is the greatest number? 
NumA= int(input("Input Number A:")) #Input from the user
NumB= int(input("Input Number B:")) #Input from the user
NumC= int(input("Input Number C:")) #Input from the user

if NumA > NumB and NumC: #If A is greater than B or C...
    print(NumA, "Is the greatest number out of the input numbers.") #print this
elif NumB > NumA and NumC: #If B is greater than A or C...
    print(NumB, "Is the greatest number out of the input numbers.") #print this
else: #If C is greater than B or A...
    print(NumC, "Is the greatest number out of the input numbers.") #print this