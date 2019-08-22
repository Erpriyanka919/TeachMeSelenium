'''
Created on 07-May-2019

@author: Priyanka.Gupta
'''
a = "Hi"
b = " I am Priyanka"
c = a + b
print(c)
sp = int(input("sp is:"))
cp = int(input("cp is:"))
if sp > cp :
    print("Profit :" , sp-cp)
if sp < cp :
    print("Loss :" , cp-sp)
if sp == cp :
    print("No Profit No loss")
    

