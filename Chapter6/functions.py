#function as argument

def add(a,b):
    return a+b
def argFunc(func,a,b):
    return func(a,b)
print(argFunc(add,3,5))

#pass in python
def fun():
    pass
fun()

#pass by value for Immutable types(integers,strings, tuples)
def update_num(num):
    num = 60
a = 20
a = 40
update_num(a)
print(a)

#pass by reference for Mutable types(lists, dicts, sets, objects)
def update_list(num):
    num.append(5)

uplist = [1,2,3]
update_list(uplist)
print(uplist)

#lambda Function
s1 = "Alertcode"
s4 = "ALERTCODE"
s2 = lambda func: func.upper()
s3 = lambda func: func.lower()
print(s2(s1))
print(s3(s4))

#list comprehension
a = [2,3,4,5]
res = [val**2 for val in a]
print(res)

#*args and **kwargs
def func(*sim):
    for k in sim:
        print(k)
func('Hello','Welcome')

def funct(**tim):
    for k, val in tim.items():
        print("%s == %s" % (k,val))
funct(s1 = 'Hello',s2 = 'Welcome')

