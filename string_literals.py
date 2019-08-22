'''
Created on 10-May-2019
string literals
@author: priyanka.gupta
'''
from _operator import not_
a = " Hello World "
print(a[1])
print(a[2:5])
print(a.strip())
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!'] 
x = ["apple", "banana"]
print("sharp" not in x)