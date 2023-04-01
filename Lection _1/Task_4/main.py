import math
a = int(input())
b = int(input())
c = int(input())

d = b**2-4*a*c
if d < 0 :
    print("There are no roots")
elif d == 0:
    print(x=-b/(2*a))
elif d > 0:
    x1=(-b+(math.sqrt(d)))/(2*a)
    x2=(-b-(math.sqrt(d)))/(2*a)  
    print(x1)
    print(x2)