'''
Created on 13-May-2019

@author: Priyanka.Gupta
'''

numa = int(input("Enter the num:"))
factors = 0
for i in range(2,numa):
    if numa % i == 0:
        factors += 1
        break
if factors == 0:
    print("This is prime number")
else:
    print("This is not prime number")
    



