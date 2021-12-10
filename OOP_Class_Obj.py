#This all about how to define a class ,methos inside a classs create an Obj of class and accessing the Obj
class Customer:
    '''This class have all info about the Customer'''
    def __init__(self,cname,vname,vbrand):
        self.cname=cname
        self.vname=vname
        self.vbrand=vbrand

    def custInfo(self):
        print('cname = ',self.cname,end=' ')
        print('vname = ', self.vname, end=' ')
        print('vbrand = ', self.vbrand)
#This is How we Create an Object of a Classs
c1=Customer('SHIVA','ACCORD','HONDA')
c2=Customer('DINESH','CAMARY','TOYOTA')
c3=Customer('ANKITH','SUPURB','SKODA')
#Accessing methods in a class
c1.custInfo()
c2.custInfo()
c3.custInfo()
#we can info of a class using DocDtring or Help
print(Customer.__doc__)
help(Customer)
#Self is like a '''this''' keyWord in java it refers to Current Instance of Class
class Student():
    def __init__(self):
        print('self points to : ',id(self))
s1=Student()
print('reference variable s1 points to : ',id(s1))
#Attributed related functions
print(hasattr(c1,'cname'))
print(getattr(c1,'cname'))
setattr(c1,'cname','shiva')
print(getattr(c1,'cname'))
delattr(c2, 'cname')
#Built-In Class Attributes
print(c1.__doc__)
print(Customer.__name__)
print(c1.__module__)
print(c1.__dict__)
