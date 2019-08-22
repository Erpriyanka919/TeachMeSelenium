'''
Created on 07-May-2019

@author: priyanka.gupta
'''
name = input("Enter the student name : ")
maths_marks = float(input("Enter the maths marks:"))
english_marks = float(input("Enter the english marks:"))
if english_marks > 90 and maths_marks >90:
    print(name,"scholarship is provided")
else:
    print(name,"scholarship is not provided")