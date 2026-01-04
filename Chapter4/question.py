#check whether the number is prime number or not
num = 1
flag = 0
if num>1:
    for i in range(2,num):
        if num%i==0:
            flag = 1
            break
    if flag == 1:
        print("Its not prime")
    elif flag == 0:
        print("Its prime")
else:
    print("Please put a number greater than one")

#calculate the factorial of the number
num = 8
factorial = 1

for i in range(5):
    