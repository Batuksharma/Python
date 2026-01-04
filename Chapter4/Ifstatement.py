temperature = 22
if temperature > 30:
    print("Its Warm")
    print("Drink Water")
elif 20<temperature<30:
    print("Maybe you should drink water")
else:
    print("Just Chill")

#short hand if and else
a = 20
b = 30

print("a>b") if a>b else print("b>a")