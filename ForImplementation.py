#This is now an Iterator works

#1st it uses iter() on iteratable obj's like list,tuple,set,str
#2nd then it uses next() to et next item from iterable Object
import sys
lis=[1,2,3,4,5,6,7,8,9,10]
itrbl_lis=iter(lis)
while True:
    try:
        print(next(itrbl_lis))
    except StopIteration:
        break
print(type(itrbl_lis))



