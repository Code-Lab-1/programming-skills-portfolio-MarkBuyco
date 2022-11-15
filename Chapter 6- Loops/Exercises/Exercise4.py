sandwich_orders = ['egg', 'waffle', 'ham', 'tuna'] #List of sandwich orders
finished_sandwiches = [] #empty list of finished sandwich

while sandwich_orders: # While loop
    current_sandwich = sandwich_orders.pop() #Removing sandwich from the list
    print("\n Would you like to taste our " + current_sandwich + " sandwich for a cheap price?")#Printed data with sentence.
    finished_sandwiches.append(current_sandwich) #adding current sandwich to finished sandwich

print("\n") #New line
for sandwich in finished_sandwiches: #For loop, to import sandwitch in finished_sandwiches
    print(" \nAre you done satisfied with our " + sandwich + " sandwich?") #Printed data with sentence.