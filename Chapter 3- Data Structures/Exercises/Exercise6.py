Guest__list= ["Iftikhar Khan", "Usman Ahmad","Elon Musk"]  #list
Invite_mes= "\n Good day! You are still invited to a dinner on Thurday \n 6pm in Burj Al Arab, room 56. \n-Mark Buyco"
#Variable message
Guest__list[2] = 'Bill Gates' #Changing the value of the last data in the list.
Mes= "We are very sorry that we only have space for two guests, \n therefore, we will invite two people only.\n we are very sorry for the inconvenience."
#Variable message
print(Mes) #print variable message
Guest__list.pop(2) # .pop removes a specfic data within a list
print(Guest__list) #printing current list, with the removed data
print("\tTo Mr.",Guest__list[0],Invite_mes) #printing data from list, plus the message.
print("\tTo Mr.",Guest__list[1],Invite_mes) #printing data from list, plus the message.
print("\tTo Mr. Bill Gates, \n We regret to inform you that you've been cut off for dinner.\n Our deepest apologies. \n- Mark Buyco") 
#printing statement only.
del Guest__list[0] #Deletes data in the list.
del Guest__list[0] #Deletes data in the list.
print(Guest__list) #Print an empty list.


