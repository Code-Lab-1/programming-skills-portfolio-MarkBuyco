def describe_city(city, country='Philippines'): #Function with the default country.
    message = city.title() + " is located in " + country.title() + "." #Formatting the message
    print(message) #Printing that message

describe_city('Manila') #Call out function, with a city
describe_city('Dubai', 'United Arab Emirates') #Call out function with a different country.
describe_city('Cavite') #Call out function, with a different city.