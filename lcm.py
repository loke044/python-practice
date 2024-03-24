a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d = min(a, b, c)
max=max(a,b,c)
if a==b==c:
    print("lcm of three numbers=",a)
else:
    f = []
    f1 = []
    g = []
    g1 = []
    h = []
    h1 = []
    for i in range(3, max + 1):
        if a % 2 == 0:
            f.append(2)
        elif a % i == 0:
            a1=int(i*(a/i))
            f.append(a1)
        else:
            f1.append(1)
        if b % 2 == 0:
            g.append(2)
        elif b % i == 0:
            b1 =int( i * (b / i))
            g.append(b1)
        else:
            g1.append(1)
        if c % 2 == 0:
            f.append(2)
        elif c % i == 0:
            c1 =int( i * (c / i))
            h.append(c1)
        else:
            h1.append(1)
    if len(f) == 0:
        f.append(1)
    if len(g) == 0:
        g.append(1)
    if len(h) == 0:
        h.append(1)
    if len(f1) == 0:
        f1.append(1)
    if len(g1) == 0:
        g1.append(1)
    if len(h1) == 0:
        h1.append(1)
    n = []
    n.extend([min(f), min(f1), min(g), min(g1), min(h), min(h1)])
    m = []
    for i in range(len(n)):
        if n[i] not in m:
            m.append(n[i])
    t = 1
    for i in range(len(m)):
        t = t * m[i]
    if(a%2==0==b%2 or b%2==0==c%2 or a%2==c%2==0):
        print("lcm of three numbers=", t * 2)
    # elif(a%c==b%c==0):
    #     print("lcm of three numbers=", t*c)
    # elif(a%b==c%b==0):
    #     print("lcm of three numbers=", t * b)
    # elif(b%a==c%a==0):
    #     print("lcm of three numbers=", t * a)
    else:
        print("lcm of three numbers=", t)



