a=[-2,1,-3,4,-1,2,1,-5,4]
c=[]
# n=int(input("enter the length of the array:"))
# for i in range(n):
#     a.append(int(input("enter the numbers:")))
# print("given array:",a)
sum=0
largest=0
r=len(a)
s=0
t=len(a)
for k in range(len(a)):
    for j in range(t):
        for i in range(s, r):
            sum = sum + a[i]
            c.append(a[i])
            print(c)
            if largest<sum:
                largest=sum
        r -= 1
        sum = 0
    t-=1
    r=len(a)
    s+=1
print("largest sum=",largest)