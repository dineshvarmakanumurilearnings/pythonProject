class Student:
    cloName='GITAM' # Static Variable

    #Constructor and have self as 1st argm
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    # Instance Method , coz its accessing instance variables and have self as 1st argm
    def getDetails(self):
        print('Student name is :',self.name,end=' & ')
        print('Student roll is ',self.roll)

    #Class Method to access class level data
    @classmethod
    def getclgdetails(cls):
        print('clg name is :',cls.cloName)

    #static Methods with ot self an cls
    def getmarks(mat,phy,chy):
        print('Total marks scored is : ',mat+phy+chy)
#s1=Student('Dinesh',6442)
#s1.getclgdetails()
#s1.getDetails()
#Student.getmarks(70,60,80)

class Employee:
    #Declaring instance variables inside a class
    def __init__(self,name,eno):
        self.name=name
        self.eno=eno
    def getsal(self):
        self.sal=100000
        print('sal is : ',self.sal)
e1=Employee('SHIVA',6442)
e1.getsal()
#declaring instance var outside class using Obj reference
e1.age=26
e2=Employee('Dinesh',692074)
e2.getsal()
#Gives all instance variables associated o that obj using __dict__
print(e1.__dict__)
print(e2.__dict__)
#static Variables
class Car:
    brand='Jaguar'
    def __init__(self):
        Car.name='XE'
    def details(self):
        Car.Pice=2000
        Car.milege=17.5
    @classmethod
    def claasmethodm1(cls):
        cls.TopSpeed=300
    @staticmethod
    def staticmethodm2():
        Car.gear='Auto/Manual'
c=Car()
c.details()
c.claasmethodm1()
Car.staticmethodm2()
print(Car.__dict__)
#Local Variables
a=100 #global var
class Test:
    a=200 #Static Var
    def m1(self):
        a=300 #local Var
        print(a)
        print(self.a)
        print(globals()['a'])
t=Test()
t.m1()








