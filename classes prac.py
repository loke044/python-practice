class family:
    def __init__(self,name,age,mobile_no):
        self.name=name
        self.age=age
        self.mobile_no=mobile_no

    def detials(self):
        return f'%s\'s age is %d and mobile number is %s'%(self.name,self.age,self.mobile_no)

m1=family('devika',43,'9043849682')
m2=family('ramana',55,'8790460722')
m3=family('lokesh',20,'8525886512')

print(m1.detials())
print(m2.detials())
print(m3.detials())




class loki:
    dad,mom='ramana','devika'
parent=loki()
print(parent.dad)

class student:
    m1,m2,m3=100,99,98
    def marks(self):
        sum=student.m1+student.m2+student.m3
        avg=sum/3
        print(sum)
        print(avg)
        return
ans=student()
ans.marks()


class no:
    def number(self,a):
        if a%2==0:
            print("the given number",a,"is even number")
        else:
            print("the given number",a, "is odd number")


digit=no()
digit.number(int(input(" give any no:")))


class no:
    def __init__(self,a):
        if a%2==0:
            print("the given number",a,"is even number")
        else:
            print("the given number",a, "is odd number")


digit=no(int(input(" give any no:")))


class sample:
    num=0
    def __init__ (self,var):
        sample.num+=1
        self.var=var
        print(self.var,sample.num)
    def __del__(self):
        sample.num-=1
        print("lefted value %d"%self.var)
a=sample(5)
a1=sample(10)
a2=sample(15)
del a,a1,a2


class sample:
    n1=1
    __n2=10
    def check(self):
        print(sample.n1)
        print(sample.__n2)
s=sample()
s.check()
print(s.n1)
#print(s.__n2)

class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        radius=self.radius
        return circle.pi*(radius**2)
    def circumference(self):
        radius = self.radius
        return 2*circle.pi*radius
r=int(input("enter the radius:"))
c=circle(r)
print(c.area())
print(c.circumference())


class string:
    upper=0
    lower=0
    vowel=0
    consonants=0
    space=0
    def __init__(self,ch):
        self.ch=ch
    def count(self):
        for i in self.ch:
            if i.isupper():
                string.upper+=1
            if i.islower():
                string.lower+=1
            if i in ('AEIOUaeiou'):
                string.vowel+=1
            if True:
                string.consonants=len(self.ch)-string.vowel-string.space
            if i.isspace():
                string.space+=1

ch=str(input("eneter any string:"))
s=string(ch)
s.count()
print("The given string contains...")
print("%d Uppercase letters"%s.upper)
print("%d Lowercase letters"%s.lower)
print("%d Vowels"%s.vowel)
print("%d Consonants"%s.consonants)
print("%d Spaces"%s.space)

class total:
    sum=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        for i in marks:
            total.sum+=i
    def display(self):
        print("{}\'s total mark={}".format(self.name, total.sum))


t=total('loki',[99,98,97,90,100])
t.display()