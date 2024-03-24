# def sum(m,n):
#  if n==0:
#     return(m)
#  elif m==0:
#      return(n)
#  else:
#     return sum(m,n-1)+1
# a,b=2,8
# print(sum(a,b))
#
# n=5
# m=2*n-1
# mid=((2*n)/2)+1
# b="  "
# for i in range(1,m+3):
#    r = m-i+3
#    if i<=n:
#     s=n+1-i
#     print(b*s,'*'*i)
#    elif i==mid:
#        print(i*'*')
#    elif  i>mid:
#        s = i - n-1
#        print(b*s,'*'*r)
#    else:
#        break


# a=1%2
# if a==0:
#     print("true")
# else:
#     print("f")
# import math
# a=str(input("enter any string:"))
# b=math.ceil(len(a)/2)
# print("middle element= "+a[b-1])

# A=[1,2,3,4,5]
# print(A)
# b=A[len(A)-1]
# A[len(A)-1]=A[0]
# A[0]=b
# print(A)
#
#
# a=str(input("enter any string:"))
# print((a[len(a)-3:len(a)])*3)
#
# r=int(input("enter no.of rows:"))
# c=int(input("enter no.of columns:"))
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         a=int(input("m"+str(i)+str(j)+"="))
#         (a)
#
# a=[-1,2,-3,4,5,6]
# b=1
# for i in range(0,len(a)):
#     if( i<len(a)-1 and ((a[i]>=0 and a[i+1]< 0 ) or (a[i]<0 and a[i+1]>=0))):
#         b=b+1
# if b==len(a):
#     print("true")
# else:
#     print("false")

# a=[[1,2],[5,6]]
# print(a[-1][1])
# a=[1,2,3,4]
# for i in range(1,len(a)+1):
#     print(a[-i])

# a="* "
# for i in range(5):
#     print(i*a)
# b=5
# for j in range(4):
#     print(a*(b-j))
#
#
# c=[['Raj', 'uayyar'], ['Suraj', 'Sharma'], ['Karan', 'Kumar'],
#    ['Jade', 'Canary'], ['Raj', 'Thakur'], ['Raj', 'Sharma'], ['Kiran', 'Kamla'],
#    ['Armaan', 'Kumar'], ['Jaya', 'Sharma'], ['Ingrid', 'Galore'], ['Jaya', 'Seth'],
#    ['Armaan', 'Dadra'], ['Ingrid', 'Maverick'], ['Aahana', 'Arora']]

# for i in range(len(c)-1):
#    for j in range(i+1,len(c)):
#       if c[i] < c[j]:
#          pass
#       else:
#          c[i], c[j] = c[j], c[i]
# print(c)

#maximum of 3 numbers:
# def maxx(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(maxx(5,10,3))

#sum of all numbers
# def summ(elements):
#     add=0
#     for i in elements:
#         add=add+i
#     return add
#
# l=[8,2,3,0,7]
# print(summ(l))

#multiply
# def mul(x):
#     multi=1
#     for i in x:
#         multi*=i
#     return multi
# print(mul([8,2,3,-1,7]))

#reverse strin
# def rev(x):
#     y=""
#     for i in range(len(x)):
#         j=len(x)-i-1
#         y+=x[j]
#     return y
# a="1234abcd"
# print(rev(a))

#factorial
# def fact(x):
#     fact=1
#     if x==0:
#         return 1
#     else:
#         for i in range(1,x+1):
#             fact*=i
#         return fact
# print(fact(5))
#
# elements = [
#         {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
#         {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
#         {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
#         {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
#     ]
# for x in 'name'[-1::-1]:
#     size = len(elements)
#     for j in range(size - 1):
#         for i in range(size - 1 - j):
#             if elements[i]['name'] >elements[i + 1]['name']:
#                 elements[i]['name'], elements[i + 1]['name']= elements[i + 1]['name'], elements[i]['name']
# print(elements)
# size=len(elements)
# for i in range(size-1):
#     for j in range(size-1):
# def insertion(val):
#     for i in range(1,len(val)):
#         pointer=val[i]
#         j=i-1
#         while j>=0 and pointer<val[j]:
#             val[j+1]=val[j]
#             j=j-1
#         val[j+1]=pointer
#
# if __name__=='__main__':
#     elements=[2,1,5,7,2,0,5]
#     stream = []
#     for x in range(len(elements)):
#         stream.append(elements[x])
#         insertion(stream)
#         a = len(stream)
#         if a%2==0:
#             index=a/2
#             print((stream[int(index)]+stream[int(index-1)])/2)
#         else:
#             index=a/2
#             print(stream[int(index)])
#
#     print(stream)

# elements = [
#     {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#     {'name': 'rajab', 'age': 12, 'time_hours': 3},
#     {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#     {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
# ]
# merged=[]
# for i in range(len(elements)):
#     elements.pop(0)
# print(elements)
# # print(merged)
#
#











# def hello():
#     print ("hello - Python")
#     return "loki"
# print(hello())

#
# def area(b,h):
#     return 0.5*b*h
# print(area(5,10))
#
# def printf(age,name):
#     print(name,age)
#     return
# printf(name="loki",age=20)

#
# def printf(name,age=20):
#     print(name,age)
#     return
# printf(name="loki")
# printf("loki",21)

#__variable__

# def name(*nos):
#     for i in nos:
#         print(i)
#     return
# name(1,2,3,4,'loki')


# x=lambda a1,a2:a1+a2
# print(x(1,2))
#
# print(x(3,8))

#
# def loc():
#     y=10
#     print(y)
#     return
# loc()
# print(y)

# c=10
# def var():
#     global c #global keyword
#     c+=1
#     print(c)
# var()

# a=[[('Jan 9', 35), ('Jan 10', 30)], [], [('Jan 1', 27)], [('Jan 2', 31)], [('Jan 3', 23)], [('Jan 4', 34)], [('Jan 5', 37)], [('Jan 6', 38)], [('Jan 7', 29)], [('Jan 8', 30)]]
# sum = 0
# num = 0
# for i in range(len(a)):
#     for index, element in enumerate(a[i]):
#         num += 1
#         sum += element[1]

# print(sum/num)
# max=0
# for i in range(len(a)):
#     for index, element in enumerate(a[i]):
#         if element[1]>max:
#             max=element[1]
# print(max)
# import csv
# arr=[]
# with open("C:\weather.csv","r") as f:
#     for row in f:
#         c=row.split(',')
#         arr.append(if int(c[1]))
# print(arr)
# # f.close()

#
# def kavi(n):
#     a=str(n)
#     max=0
#     for i in a:
#         if int(i)>=max:
#             max=int(i)
#     print(int(str(max)+a.replace(str(max),"")))
#     return
#
# if __name__=='__main__':
#     n=23756
#     result=kavi(n)
#     print(result)

























































































































