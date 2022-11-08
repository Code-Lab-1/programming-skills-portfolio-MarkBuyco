Math= int(input("Enter your marks in Math")) #Getting marks from users in math
Science= int(input("Enter your marks in Science")) #Getting marks from users in science
English= int(input("Enter your marks in English")) #Getting marks from users in english
CodeLab= int(input("Enter your marks in Codelab")) #Getting marks from users in codelab
Design= int(input("Enter your marks in Design")) #Getting marks from users in design

marks_obtained= Math+ Science+ English+ CodeLab+ Design #Adding all marks
average= (marks_obtained)/5 #Dividing marks into 5 to get the average
print("Total Marks=", marks_obtained) #print total marks
print("Average=",average) #print average
