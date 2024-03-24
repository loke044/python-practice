n=int(input("n="))
d=0
for i in range(2,n+1):
    for j in range(2,n+1):
        for k in range(2,n+1):
            a=i**2
            b=j**2
            c=k**2
            if a+b==c and a<b<c:
                print(a,b,c)
                d+=1
print(d)
