# a=[9,1,3,200,7,4,10,5]
# for j in range(0,len(a)):
#     for i in range(0, len(a) - 1):
#         if a[i] > a[i + 1]:
#             b = a[i]
#             a[i] = a[i + 1]
#             a[i + 1] = b
#         else:
#             continue
# d=[]
# c=1
# for i in range(0,len(a)-1):
#     if a[i+1]-a[i]==1:
#         c+=1
#         d.append(a[i])
#         d.append(a[i+1])
#     else:
#         continue
# print(a)
# print(d)
# if c>1:
#     print("The longest consecutive element sequence is :", d)
#     print("length: ", c)
# else:
#     print("There is no consecutive element sequence")
#
