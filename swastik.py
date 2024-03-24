n=int(input("n="))
print("\n")
for i in range(1,n+1):
    if i==1:
        print("* "+"  "*(n-3)," *"*n)
    elif i>1 and i<n:
        print("* "+"  "*(n-3)," *")
    else:
        print("* "+"* "*(n*2-2))
for j in range(1,n):
    if j<n-1:
        print("  " * (n - 2), " *","  "*(n-3)," *")
    else:
        print("* "*n,"  "*(n-3),"*")

