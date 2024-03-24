# class bst:
#     def __init__(self,key):
#         self.key=key
#         self.lhs=None
#         self.rhs=None
#
#     def insert(self,data):
#         if self.key==None:
#             self.key=data
#             return
#         elif self.key==data:
#             return
#         elif data<self.key:
#             if self.lhs:
#                 self.lhs.insert(data)
#             else:
#                 self.lhs=bst(data)
#         elif data>self.key:
#             if self.rhs:
#                 self.rhs.insert(data)
#             else:
#                 self.rhs=bst(data)
#
#     def preorder(self):
#         print(self.key)
#         if self.lhs:
#             self.lhs.preorder()
#         if self.rhs:
#             self.rhs.preorder()
#
#     def inorder(self):
#         if self.lhs:
#             self.lhs.inorder()
#         print(self.key,end=" ")
#         if self.rhs:
#             self.rhs.inorder()
#
#     def postorder(self):
#         if self.lhs:
#             self.lhs.inorder()
#         if self.rhs:
#             self.rhs.inorder()
#         print(self.key, end=" ")
#
#
#     def find_max(self):
#         if self.rhs is None:
#             return self.key
#         return self.rhs.find_max()
#         a=find_max()
#         print(a)
#
#
#     def find_min(self):
#         if self.lhs is None:
#             return self.key
#         return self.lhs.find_min()
#
#     def delete(self,data):
#         if data<self.key:
#             if self.lhs:
#                 self.lhs.delete(data)
#
#         elif data>self.key:
#             if self.rhs:
#                 self.rhs.delete(data)
#         else:
#             if self.lhs is None and self.rhs is None:
#                 return None
#             if self.lhs is None:
#                 return self.rhs
#             if self.rhs is None:
#                 return self.lhs
#
#             mini = self.rhs.find_min()
#             self.key =mini
#             self.rhs = self.rhs.delete(mini)
#
#         return self
#
#
#
#
# root=bst(10)
# lst=[5,20,22,30,7,15]
# for i in lst:
#     root.insert(i)
#
# print(root.inorder())
# # print(root.find_max())
# # print(root.find_min())
# print(root.delete(7))
# print(root.inorder())
#







# matrix=[[1,2,3,1,2],[4,5,6,2,3],[7,8,9,3,4]]
# row=3
# column=5
# # row=int(input("row size:"))
# # column=int(input("column size:"))
# # print("enter the elements row wise:")
# # for r in range(row):
# #     a=[]
# #     for c in range(column):
# #         a.append(int(input()))
# #     matrix.append(a)
# # print("given matrix")
# # print("matrix")
# k=[]
# for j in range(row):
#     for i in range(column):
#         k.append(matrix[j][i])
#
# y=len(str(max(k)))
# for r in range(row):
#     for c in range(column):
#         x=matrix[r][c]
#         print(x," "*(y-len(str(x))),end=" ")
#     print()
# s=0
# print("\n\n")
# d=[]
# m=column
# if row!=column:
#     if column<row:
#         for j in range(0,column):
#             e = []
#             for i in range(0,column - s):
#                 e.append(matrix[i][column - i - s - 1])
#             d.append(e)
#             s += 1
#     else:
#         for j in range(0,column):
#             e = []
#             for i in range(0,row):
#                 e.append(matrix[i+s][column-s-1])
#                 s+=1
#             d.append(e)
#             s += 0
#
#
# else:
#     for j in range(0, len(matrix)):
#         e = []
#         for i in range(0, len(matrix) - s):
#             e.append(matrix[i][column - i - s - 1])
#         d.append(e)
#         s += 1
#
# print(d)
#
# f=[]
# for k in range(1,len(d)+1):
#     f.append(d[-k])
# print(f)
# s=len(f)
# for j in range(0,len(f)):
#     for i in range(0,len(f)-s+1):
#         v=f[j][i]
#         print(v," "*(y-len(str(v))),end=" ")
#     s-=1
#     print()
# s=0
# if row!=column:
#     if column<row:
#         for j in range(1, row):
#             for i in range(0,column):
#                 if j==row-1 and i==column-1:
#                     continue
#                 else:
#                     w = matrix[j + s][column - i - 1]
#                     print(w, " " * (y - len(str(w))), end=" ")
#                     s += 1
#
#             print()
#             s=0
#     else:
#         for j in range(1,column):
#             for i in range(0,row-s):
#                 w = matrix[i + s][column + i-1]
#                 print(w, " " * (y - len(str(w))), end=" ")
#             print()
#             s += 1
#
# else:
#     for j in range(1, len(matrix)):
#         for i in range(1, len(matrix) - s):
#             w = matrix[i + s][row - i]
#             print(w, " " * (y - len(str(w))), end=" ")
#         print()
#         s += 1
#
#









