0,1,1,2,3,5,8,13
def fib(a,b,n):
    while n>0:
        yield a+b
        b=a+b
        a=b-a
        n -=1
a,b=0,1
print(a,b,end=' ')
for x in fib(a,b,10):
    print(x,end=' ')
#Fibenocciee Series using list comprehension
mylis=[0,1]
[mylis.append(mylis[-2]+mylis[-1])for x in range(11)]
print(mylis)
#Reverse a string word wise
str1='This need to be reversed by word wise order using list Comprehension'
revstr=' '.join([x[::-1]for x in str1.split()])
print(revstr)
#This is to find out ovels and their Occurance in a given string
rawstr='This is to find out vowels and their occurrence in a given string'
print({(x,rawstr.count(x))for x in rawstr if x=='a' or x=='e'or x=='i'or x=='o' or x=='u'})
