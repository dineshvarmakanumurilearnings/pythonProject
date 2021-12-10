#string is immutable in nature
s='this is a string'
#capitalize is used to make 1st chat Caps
captalize=s.capitalize()
print('capitalize() ---> ',captalize)
#UpperCase and LowerCase
upper=s.upper()
lower=s.lower()
print('upper() ---> ',upper)
print('lower() ---> ',lower)
#Used to swapCase of chars in string
swapbefore='this is a NEW STRING'
afterswapcase=swapbefore.swapcase()
print('before swapcase -->',swapbefore)
print('swapCase() -->',afterswapcase)
#Counts the occcurences of a char in a string
print('count of char "i" in a given string',s.count('i'))
#Used to split the string by "space" by default
lis=s.split()
print('split() ---> ',lis)
#lenght of a string
print('len(s) ---> ',len(s))
