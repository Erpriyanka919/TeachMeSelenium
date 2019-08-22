'''
Created on 08-May-2019
TO find some of fractional series a + a/2 +a/3 + a/4 +...+ a/N
@author: priyanka.gupta
'''
n = int(input("Enter the number n : "))
a = int(input("Enter the number a : "))
sum=0

for num  in range(1,n+1):
    sum = sum + a/num
    print(sum)
print("Sum of fraction numbers from", a , "to" , a ,"/",n, "is" ,sum)