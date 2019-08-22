'''
Created on 10-May-2019
list examples
@author: priyanka.gupta
'''
# to print list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# To access the list items by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#You can loop through the list items by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list") 

#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# TO add item in the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To add an item at the specified index, use the insert() method:
#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

