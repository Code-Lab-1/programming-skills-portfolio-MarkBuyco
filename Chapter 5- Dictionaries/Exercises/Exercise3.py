#Dictionary of words
Glossary= {"Variables":"are data that are stored with an assigned name."
           , "Strings":"is a collection of words and any letter in the alphabet."
           , "Print":"Basically prints results to the screen"
           , "List":"is a data type that can store a collection of values"
           , "If statements":"Set of program that deals with the control flow."
           , "Boolean":"Thoughts that can be evaluated by true or false."
           ,"Comment":"Are notes you can leave that doesn't affect the code."
           ,"Float":"A numerical value that has decimal."
           , "Loop":"Set of program that can go through items one by one. "
           , "Input":"A code for python to get input from the users."
           } # End of ditionary, 10 terms.

for word, definition in Glossary.items(): #Using for loop that goes through the dictionary
    print("\n" + word + ": " + definition) #Print the dictionary words and definition, then repeat. 