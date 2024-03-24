# class person:
#     family="perugumi"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name+'\'s age is',self.age,"and his family name is "+person.family)
#
# person1=person("loki",21)
# person2=person("ramana ",55)
# person1.display()
# person2.display()

# inheritance
#
# class ece():
#     def students(self):
#         print("eceians")
#
# class a(ece):
#     def staffs(self):
#         print("good")
#
# class b(a):
#     def faculty(self):
#         print("fellows")
#
# e=b()
# e.students()
# e.staffs()
# e.faculty()

# multiple inheritance
#
# class land():
#     def display(self):
#         print("this animal lives in land")
#
# class water():
#     def printt(self):
#         print("this animal lives in water")
#
# class frog(land,water):
#     pass
#
# f=frog()
# f.display()
# f.printt()

# encapsulation
# private methods
#
# class classroom:
#     __count=0
#     def __init__(self):
#         self.__count=30
#         print(self.__count)
#     def boys(self,countt):
#         self.__count=countt
#         print(self.__count)b
#
# b=classroom()
# b.boys(1000)

# polymorphism

class dog:
    def sound(self):
        print("bow bow")
class cat:
    def sound(self):
        print("meaw")

def pet(animal):
    animal.sound()
a=dog()
b=cat()
pet(a)
pet(b)





















