import calc as c
a =12
b=7


def module(a,b):
    return a%b

print(f"addition of {a} and {b} is "+ str(c.add(a,b)))
print(f"Subtraction of {a} and {b} is "+str(c.sub(a,b)))
print(f"Multiplciation of {a} and {b} is "+str(c.mul(a,b)))
print(f"division of {a} and {b} is "+str(c.div(a,b)))
print(f"modulo of {a} and {b} is "+str(module(a,b)))