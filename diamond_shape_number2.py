n=int(input("n="))
a=""
for i in range(1,n+1):
    j=str(i)+" "
    a=a+j
d="  "
b=0
for j in range(n+1):
    c=n-j-1
    if j==0 and b<n*2:
        print(d * c + a[0])
        b = b + 2
    elif j>=1 and c>=0 and b<n*2:
        print(d*c+a[0]+d*b+a[b])
        b = b + 2
    else:
        continue
c=len(a)-4
for k in range(n):
    e=n-k-1
    if k==n-1:
        print(d * k + a[0])
    elif k>0:
        print(d * k + a[0] + d * e*2 + a[c])
        c = c - 2
    else:
        continue

