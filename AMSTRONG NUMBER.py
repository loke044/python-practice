# for i in range(1,1001):
#     a=str(i)
#     b=0
#     for j in range(len(a)):
#         b+=(int(a[j]))**3
#     if b==i:
#         print(i)
#         b=0
#     else:
#         b=0

a=int(input("enter any number: "))
b=str(a)
c=0
for i in b:
    c+=int(i)**len(b)
print(a, "is amstrong number.") if c==a else print(a,"is not amstrong number")

