A="THIS IS A PYTHON LANGUAGE"
# C=0
# for i in range(C,len(A)):
#     if A[i]==" ":
#         D=A[C:i]
#         C=i+1
#         if len(D)%2==0:
#             print(D)
#     elif i==len(A)-1:
#         E=A[C:i+1]
#         if len(E)%2==0:
#             print(E)
#         break
b=A.split()
for i in b:
    if len(i)%2==0:
        print(i)

