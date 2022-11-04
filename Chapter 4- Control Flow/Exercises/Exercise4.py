#If-ELif-Else Age
age= int(input("Enter A Person's Age")) #Ask user of a specific age
if age < 2: #if statement
    print("That person is a baby.") #print if the codition above is met.
elif age < 4: #elif statement 1
    print("That person is a toddler.") #print if the codition above is met.
elif age < 13: #elif statement 2
    print("That person is a kid.")
elif age < 20: #elif statement 3
    print("That person is a teenager!") #print if the codition above is met.
elif age < 65: #elif statement 4
    print("That person is an adult!") #print if the codition above is met.
else: #else statement 
    print("That person is an elder!") #print if the none of codition above is met.