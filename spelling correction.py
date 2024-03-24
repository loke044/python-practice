# A="lokesi"
# print(A)
# B=int(input("enter index position:"))
# C=str(input("letter to be replace:"))
# D=""
# for i in range(len(A)):
#     if i==B:
#         D=D+C
#     else:
#         D=D+A[i]
# print(D)

A="THIS IS A LANGUAGE"
print(A)
C="PYTHON"
print(C)
B=int(input("enter index position:"))
D=""
for i in range(len(A)):
    if i==B:
        D=A[0:i+1]+C+A[i:len(A)+1]
print(D)