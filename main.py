lis=(x**2 for x in range(1,10))
print(type(lis))
#for x in lis:print(x)

def sqrgen(n):
    yield n**2
    n -=1
#for x in sqrgen(1000000000):print(x)
y=sqrgen(10)
print(type(y))





















