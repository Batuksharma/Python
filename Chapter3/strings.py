#METHODS IN PYTHON 

name = "batuk"
print(len(name)) # prints the length of the string
print(name.endswith("uk")) #checks whether it ends with the given string
print(name.startswith("uk")) #checks whether it starts with the given string
print(name.capitalize())  # only capitalises the initial letter of first word
print(name.upper()) # converts all letters to upper case
print(name.lower()) # converts to lower case
print(name.strip()) # removes leading and trailing spaces
print(name.lstrip()) # removes leading spaces
print(name.rstrip()) # removes trailing spaces
print(name.find("uk")) #returns the index of the first occurrence of the given string
print("pro" in name) #checks whether the given string is present in the string
print("pro" not in name) #checks whether the given string is not present in the string

name1 = "Alertcode is a company"
print(name1[1:5]) # prints the characters from index 1 to 5 (5 is excluded)
print(name1.replace("Alertcode", "Lifessentials")) #replaces the string

name2 = "Alertcode"
print(name1[1:8:2]) # prints the characters from index 1 to 8 with a step of 2  

first = 'Batuk'
last = 'Sharma'
message = f'{first} [{last}] is a coder' # f string formatting
message1 = f'{len(first)} {2+2}'  # This is called formatted string
print(message)
print(message1) # prints the result of the expression inside the curly brackets
