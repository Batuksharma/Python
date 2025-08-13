#Problem1
name = input("Enter your name: ") # Get user's name
print(f"Good Morning,{name}") # Print a greeting with the user's name

letter = '''Dear name,
            You are selected.
            Date'''           # Define a multi-line string

print(letter.replace("name","Batuk").replace("Date","24/6/2025")) # strings are immutable, this function does not change the original string, it prints the new string


#Problem2
text = "Alertcode is a great company"
print(text.find("c")) # this returns index if found, e;se it returns -1


#Problem3
sentence = "Dear Batuk,\nThis python course is amazing,\nThanks" # Define a string with a newline character
print(sentence)

