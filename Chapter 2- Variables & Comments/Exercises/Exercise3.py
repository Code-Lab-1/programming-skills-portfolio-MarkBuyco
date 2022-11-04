Name= "\tMark\tJerome \n \tBuyco\t" # Variable with white spaces.
print(Name)

Name= "----Mark Jerome Buyco----" #New variable.
print(Name.lstrip('-'),"\n.strip()\n-Remove left line") #lstrip, remove leading whitespaces.
print(Name.rstrip("-"),"\n.rtrip()\n-Remove right line") #rstrip, remove trailing whitespaces.
print(Name.strip("-"),"\n.strip()\n-Remove both left and right lines") #strip, remove leading and trailing whitespaces.
