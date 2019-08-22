'''
Created on 08-May-2019
TO print sum of odd numbers from 1 to 20
@author: priyanka.gupta
'''
sum = 0
print("Print Odd Numbers")
for num  in range(1,21,2):
    print(num)
    sum = sum + num
    
print("Sum of Odd Numbers from 1 to 20 is :" , sum)
