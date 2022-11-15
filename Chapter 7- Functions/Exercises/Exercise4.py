def make_shirt(size= 'large', message= 'I love Python!'): #function with 2 arguments, modified
    print("\n The size of the shirt is " + size + ".") #printing the size plus a setence,1st argument.
    print("It will contain these words: " + message) #printing the message on the shirt, 2nd argument.

make_shirt() #Call out the function
make_shirt(size='medium') #Call out function with different size, which means same message.
make_shirt('5XL', 'CODING IS EASY!') #Call out function, with different size and message