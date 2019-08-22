'''
Created on 09-May-2019
To print factorial
@author: priyanka.gupta
'''
factorial= int(input("Enter the number:"))
counter =1
while factorial > 1:
    counter *= factorial
    factorial -= 1
print("Factorial of the number is :" , counter)
    
    
    

