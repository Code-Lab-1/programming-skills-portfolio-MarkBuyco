prompt = "How old are you?" #asking users for their age
prompt += "\nEnter 'quit' when you are done availing. " #Entering quit to end program

while True: #While loop
    age = input(prompt) #Variable that include age of user
    if age == 'quit': #If statment, if users input quit, it will end the program
        break #End loop
    age = int(age) #Taking input age from the user

    if age < 3: # if age is less than 3
        print("No charges, you go in for free.")# if statement above is true, print this.
    elif age < 13: # if age is less than 13
        print("$10 to pay.") # if statement above is true, print this.
    else: #Else block, people aging above 13
        print("$15 to pay.") # if the user is above 13
        