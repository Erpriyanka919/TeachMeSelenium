'''
Created on 08-May-2019
sum of series like 1-2+3-4+5...n
@author: priyanka.gupta
'''
N = int(input("Enter the number : "))
sum = 0
for num  in range(1,N+1):
    if num % 2 == 0 :
        sum -= num
        print(sum)
    else :
        sum += num
        print(sum)

print("Sum of such series is" ,sum)
