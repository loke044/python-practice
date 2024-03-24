ex=[2200,2350,2600,2130,2190]
month=["january","february","march","april","may"]
j=0
k=0
for i in range(len(month)):
    if month[i]=="january":
        j=i
    if month[i]=="february":
        k=i
print(abs(ex[j]-ex[k]))
print(sum(ex[:3]))
for i in range(len(ex)):
    if ex[i]==2000:
        print(month[i])
m,ex1=input("month name:"),input("expense:")
month.append(m)
ex.append(int(ex1))
print(ex)
print(month)

d=[]
for i in range(len(month)):
    f=[]
    if month[i]=="april":
        ex[i]=ex[i]-200

    f.extend([month[i],ex[i]])
    d.append(f)
print(dict(d))





