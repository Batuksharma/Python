#Problem1
name = input("Enter your name: ")
print(f"Good Morning,{name}")

letter = '''Dear name,
            You are selected.
            Date'''

print(letter.replace("name","Batuk").replace("Date","24/6/2025")) # strings are immutable, this function does not change the original string, it prints the new string


#Problem2
text = "Alertcode is a great company"
print(text.find("c")) # this returns index if found, e;se it returns -1


#Problem3
sentence = "Dear Batuk,\nThis python course is amazing,\nThanks"
print(sentence)

