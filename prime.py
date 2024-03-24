a=int(input("beginning: "))
b=int(input("ending: "))
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
        print(i,end=" ")
        d.append(i)
if len(d)==0:
    print("no prime numbers")