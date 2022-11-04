sandwich_orders = ['pastrami','egg','pastrami', 'waffle', 'pastrami','ham', 'tuna'] #List of sandwich orders added 3 pastrami 
finished_sandwiches = [] #empty list of finished sandwich

print(" \n Sorry, we've run out of pastrami today, would you like to order something else?") #Message to inform there is no pastrami.
while 'pastrami' in sandwich_orders: #While loop to import pastrami.
    sandwich_orders.remove('pastrami') #removes pastrami in the list

while sandwich_orders: # While loop
    current_sandwich = sandwich_orders.pop() #Removing sandwich from the list
    print("\n Would you like to taste our " + current_sandwich + " sandwich for a cheap price?")#Printed data with sentence.
    finished_sandwiches.append(current_sandwich) #adding current sandwich to finished sandwich

print("\n") #New line
for sandwich in finished_sandwiches: #For loop, to import sandwitch in finished_sandwiches
    print(" \nAre you done satisfied with our " + sandwich + " sandwich?") #Printed data with sentence.
