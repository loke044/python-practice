a=str(input("enter any a password:"))
c = 0
for i in a:
    if i.isdigit():
        c += 1
if len(a)>9 and a.isalnum() and c>1:
    print("valid password")
else:
    print("!!!Invalid password!!!")