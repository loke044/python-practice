a=float(input("enter any decimal point number:"))
b=int(a)
c=a-b
#ceiling
if c==0:
    print("ceil value=", a)
else:
    d = int(a + 1)
    print("ceil value=", d)
#rounding
if c<0.5:
    print("round value=",b)
else:
    e=a+1-c
    print("round value=",e)

