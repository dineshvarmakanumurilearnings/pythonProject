def evenDecor(func):
    def inner(n):
        if func(n) == True:print(n,'is an Even Number')
        else:print(n,'is an Odd Number')
    return inner

@evenDecor
def isEven(n):
    if n%2==0: return True

isEven(12)





