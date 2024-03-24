a=str(input("enter the string:"))
b=""
for i in range (len(a)):
    if a[i]in b:
        continue
    else:
        b=b+a[i]
f=""
for j in range(len(b)):
    count=a.count(b[j])
    d=str(count)
    print("{}:{}".format(b[j],count))
    f=f+b[j]+d
print(f)

