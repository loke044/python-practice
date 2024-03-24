n=5
for i in range(1,n+1):
    a=n-i
    b=i-3
    c=n*3
    if i==1:
        print("  "*a,"@")
    elif i==n:
        print("  ",end="")
        print("@"*c)
    elif i==2:
        print("  " * a, "@  ", "@")
    else:
        print("  " * a, "@", "    " * b, "     @")
