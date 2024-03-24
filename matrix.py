rot=[]
def R():
        t = []
        t.clear()
        for c in range(column):
            b = []
            for r in range(1, row + 1):
                b.append(matrix[-r][c])
            t.append(b)
        rot.clear()
        for i in t:
            rot.append(i)
            matrix.append(i)

def Q():
    print("enter the matrix position you want to see :")
    r1, c1 = (int(input("row:")), int(input("column:")))
    print(matrix[r1][c1])

def U():
    print("enter the matrix position you want to change:")
    r1, c1, v = (int(input("row:")), int(input("column")), int(input("value to be change:")))
    matrix[r1][c1] = v
    for r in range(row):
        for c in range(column):
            print(matrix[r][c], end=" ")
        print()
print("*****THE MATRIX*****")
row=int(input("row size:"))
column=int(input("column size:"))
matrix=[]
print("enter the elements row wise:")
for r in range(row):
    a=[]
    for c in range(column):
        a.append(int(input()))
    matrix.append(a)
print("given matrix")
for r in range(row):
    for c in range(column):
        print(matrix[r][c],end=" ")
    print()
count=0
while True:
     choice=int(input("\nenter the choice 1.display desired position value 2.update the value in desired position 3.rotate 4.quit\n"))
     if choice==1:
         Q()
     elif choice==2:
         U()
     elif choice==3:
         count+=1
         if row == column:
             print("matrix after rotation")
             R()

             for r in range(row):
                 for c in range(column):
                     print(rot[r][c], end=" ")
                 print()

         else:
             print("\"rotation only works in square matrix\"")
     elif choice==4:
         for i in range(count):
             R()

         print("after all rotation")
         for r in range(row):
             for c in range(column):
                 print(rot[r][c], end=" ")
             print()

         print("-1")
         break
     else:
         print("enter the correct choice")

