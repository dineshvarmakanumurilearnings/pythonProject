import sys
class Customer:
    bankName ='HDFC'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposite(self,amt):
        self.balance=self.balance+amt
        print('Balance After Deposite',self.balance)
    def withDraw(self,amt):
        if amt>self.balance:
            print('insufficent funds......')
            sys.exit()
        self.balance=self.balance-amt
    def balanceCheck(self):
        print('The available Balance is : ',self.balance)

#Ops starts here
print('Welcome to ',Customer.bankName)
name, tri='',3
while name=='' and tri>=0 :
    if tri == 0:
        print('Transcation failed .....')
        sys.exit()
    print('plz enter you name to proceed')
    name = input('Pls Enter your Name.....')
    tri -=1
cust = Customer(name)
print('Balance-Check : B','WithDarw : W','Deposit : D',sep=' ')
touch=input('pls enter valid option : ')
if touch.upper()=='B':
    cust.balanceCheck()
elif touch.upper()=='W':
    amt =eval(input("Enter amount need to be with Drawn : "))
    cust.withDraw(amt)
elif touch.upper()=='D':
    amt = eval(input("Enter amount need to be Deposited : "))
    cust.deposite(amt)
else:
    print('plz... select valid option')



