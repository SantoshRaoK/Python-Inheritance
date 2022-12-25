# class laptop():
#     def __init__(self,company,model,price,ram):
#         self.a=company
#         self.b=model
#         self.c=price
#         self.d=ram
#     def my(self):
#         print("Company:",self.a)
#         print("Model:", self.b)
#         print("Price:", self.c)
#         print("Ram:", self.d)
# lc=input("Enter the Company name:")
# lm=input("Enter the model:")
# lp=input("Enter Price:")
# lr=input("Enter the Ram")
# new=laptop(lc,lm,lp,lr)
# new.my()

# class car():
#     def __init__(self,company,price,year,colour):
#         self.a=company
#         self.b=year
#         self.c=colour
#         self.d=price
#     def vehicle(self):
#         print("Company:",self.a)
#         print("year:",self.b)
#         print("colour:",self.c)
#         print("price:",self.d)
# cc=input("Please enter the company: ")
# cy=input("Please enter the year: ")
# cr=input("please enter the coulour: ")
# cp=input('please enter the price')
# sant=car(cc,cy,cr,cp)
# sant.vehicle()


#single Inheritance


# class parent:
#     def parentclass(self):
#         print("This is a parent class")
# class child(parent):
#     def childclass(self):
#         print("This is a child class")
# a=child()
# a.parentclass()
# a.childclass()


#multilever inheritance


# class father:
#     def fatherclass(self):
#         print("This is a father class")
# class mother():
#     def motherclass(self):
#         print("This is a mother class")
# class child(father,mother):
#     def childclass(self):
#         print("This is a child class")
# c=child()
# c.fatherclass()
# c.motherclass()
# c.childclass()


# Multi level inheritance


# class grandfather:
#     def gf(self):
#         print("This is grandfather")
# class father(grandfather):
#     def fa(self):
#         print("This is father")
# class child(father):
#     def ch(self):
#         print("This is child")
# c=child()
# c.gf()
# c.fa()
# c.ch()

#Hierarchal inheritance

class parent:
    def parentclass(self):
        print("Father name is Ravi")
class child1(parent):
    def childclass1(self):
        print("child1 name is sandhya")
class child2(parent):
    def childclass2(self):
        print("Child2 name is santosh")
obj1=child1()
obj2=child2()
obj1.parentclass()
obj1.childclass1()
obj2.parentclass()
obj2.childclass2()