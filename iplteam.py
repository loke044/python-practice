n=int(input("no.of matches:"))
a=[]
b=[]
win=[]
loss=[]
draw=[]
for j in range(n):
    t1=str(input("enter team1:"))
    t2 = str(input("enter team2:"))
    a.append(t1)
    a.append(t2)
    result=str(input("enter the result(win/ loss/ draw):"))
    if result=="win":
        win.append(t1)
        loss.append(t2)
    elif result=="loss":
         loss.append(t1)
         win.append(t2)
    else:
        draw.append(t1)
        draw.append(t2)

for i in range (len(a)):
    if a[i]in b :
        continue
    else:
        b.append(a[i])

f=[]
p=[]
w=[]
l=[]
d=[]
e={}
for j in range(len(b)):
    count=a.count(b[j])
    f.append(count)
    wins=win.count(b[j])
    w.append(wins)
    losses=loss.count(b[j])
    l.append(losses)
    draws=draw.count(b[j])
    d.append(draws)
    p.append(wins*2+draws)

for i in range(len(b)):
   t=f"Team: %s, matches played:%s, won:%s, loss:%s, draw:%s, points:"%(b[i],f[i],w[i],l[i],d[i])
   e[t]=p[i]

x=sorted(e.items(),key=lambda x:x[1],reverse=True)
y=dict(x)
for i in y:
    print(i,y[i])

