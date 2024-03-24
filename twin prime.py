a=int(input())
b=int(input())
d=[]
for i in range(a,b+1):
    c=0
    if i == 2:
        c += 1
    else:
        for j in range(2, b + 1):
            if i % j == 0 and i % 2 != 0:
                c += 1
    if c==1:
        d.append(i)
if len(d)==0:
    print("no prime numbers")
for j in range(len(d)-1):
    f=d[j]
    g=d[j+1]
    if g-f==2:
        print("(",f,",",g,")")