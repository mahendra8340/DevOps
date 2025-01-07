import sys as s
a=s.argv[1]
b=s.argv[2]

if(a<b):
    print(f"{a} is less than {b}")
elif(a>b):
    print(f"{a} is greater than {b}")
elif(a==b):
    print(f"{a} is equals to {b}")
else:
    print("invalid data")