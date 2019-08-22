'''
Created on 08-May-2019
TO find some of fractional series 1 + 1/2 +1/3 + 1/4 +...+ 1/n
@author: priyanka.gupta
'''
N = int(input("Enter the number : "))
sum = 0
for num  in range(1,N+1):
    sum = sum + 1/num
    print(sum)
print("Sum of fraction numbers from 1 to 1/",N, "is" ,sum)
