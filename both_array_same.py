A=[1,2,3,4]
B=[1,2,3,4]
c=0
for i in range(len(A)):
    if A[i]!=B[i]:
        print("both are not same.")
        c+=1
        break
if c==0:
    print("both are same")

