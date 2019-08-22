'''
Created on 07-May-2019

@author: Priyanka.Gupta
'''
marks = int(input("Percentage Marks : "))
if marks >= 90 :
    print("Grade : A+")
if marks < 90 and marks >= 80 :
    print("Grade : A")
if marks < 80 and marks >=60 :
    print("Grade : B")
if marks < 60 and marks >=50 :
    print("Grade : C")    
if marks < 50 :
    print("Grade : D")
    