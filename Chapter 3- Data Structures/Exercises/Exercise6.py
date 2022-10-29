Guest__list= ["Iftikhar Khan", "Usman Ahmad","Elon Musk"]
Invite_mes= "\n Good day! You are still invited to a dinner on Thurday \n 6pm in Burj Al Arab, room 56. \n-Mark Buyco"
Guest__list[2] = 'Bill Gates'
Mes= " Unfortunately, we are very sorry that we only have space for two guests, \n therefore, we will invite two people only.\n we are very sorry for the inconvenience."
print(Mes)
Guest__list.pop(2)
print(Guest__list)
print("\tTo Mr.",Guest__list[0],Invite_mes)
print("\tTo Mr.",Guest__list[1],Invite_mes)
print("\tTo Mr. Bill Gates, \n We regret to inform you that you've been cut off for dinner.\n Our deepest apologies. \n- Mark Buyco")
del Guest__list[0]
del Guest__list[1]
print(Guest__list)