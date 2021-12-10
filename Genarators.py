import sys
lis=[1,2,3,4,5,6,7,8,9,10]
print(sys.getsizeof(lis))
y=filter(lambda i: i%2==0,lis) #here filter,map,reduce are iteratores by default
print(y.__next__())
print(next(y))
#for x in y:print(x)

def gen(n): #Here gen is an genarator
    while n>0:
        yield n**2
        n -=1

print(sys.getsizeof(gen(10)))
for z in gen(10):print(z)
