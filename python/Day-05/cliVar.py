import calc as c
import sys as s

a=float(s.argv[1])
b=float(s.argv[3])
op=s.argv[2]

if op=="add":
    print(f"addition of {a} and {b} is "+ str(c.add(a,b)))
elif op=="sub":
    print(f"Subtraction of {a} and {b} is "+str(c.sub(a,b)))
elif op=="div":
    print(f"division of {a} and {b} is "+str(c.div(a,b)))
elif op=="mul":
    print(f"Multiplciation of {a} and {b} is "+str(c.mul(a,b)))
