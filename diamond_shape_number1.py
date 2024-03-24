n=5
for i in range(1,n+1):
    a = n - i
    print("\n"+"  "*a,end="")
    for j in range(1,i+1):
        print(j,end="   ")

for k in range(1,n+1):
    print("\n" + "  " * k, end="")
    for l in range(1,n-k+1):
        print(l, end="   ")