prompt = "\n What topping would you like to add more?"#Prompt to take input from users
prompt += "\nEnter 'quit' when you don't want to add anything else: " #Prompt to end, if user wish to quit

while True: #While loop
    tops = input(prompt) #Variable that contains the topping which is from the user.
    if tops != 'quit': #If the user is not equal to quit, it will loop again and again.
        print("We'll add" + tops + " to your pizza.") # Printed statement.
    else:#Else block
        break #Break is stoping the loop.