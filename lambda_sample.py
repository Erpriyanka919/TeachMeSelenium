'''
Created on 15-May-2019

@author: Priyanka.Gupta
'''
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

y = lambda a, b : a * b
print(y(5, 6))

def myfunc3(n):
    return lambda a : a * n

mydoubler = myfunc3(2)
mytripler = myfunc3(3)

print(mydoubler(11))
print(mytripler(11))