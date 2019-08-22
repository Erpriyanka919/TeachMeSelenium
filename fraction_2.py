'''
Created on 08-May-2019
TO find some of fractional series 1/a + 2/a + 3/a + 4/a +...+ N/a
@author: priyanka.gupta
'''
n = int(input("Enter the number n : "))
a = int(input("Enter the number a : "))
sum=0

for N in range(1,n+1):
    sum = sum + N/a
    print(sum)
print("Sum of fraction numbers from", N , "to" , N ,"/",a, "is" ,sum)