"""
Here some of the questions that will be solved : 
1. Create an array and traverse . 
2. Access individual elements through indexes. 
3.append any value to the arrray using append() method
4.Insert values in an array using insert() method 
5.Extend python array using extend method 
6.add items from list into array using fromlist()
7.Remove last array element using pop()
8.fetch any element through its index using index() method 
10.Reverse a ython array using reverse method 
11.get array buffer information through buffer_info() method 
12.Check for number of occurrences of an element using count() method 
13.Convert array to string using tostring method 
14.convert arrray to a pythonn list with same elements using todolist method 
15.append a string to char array using fromstring() method 
16.slice element from an array.
"""

from array import * 
# 1. Create an array and traverse . 
my_array = array('i',[1,2,33,44,55,6])

for i in my_array: 
    print(i)


# 2. Access individual elements through indexes. 

# print("Question no : 2")
# arr1 = array('i',[2,12,44,25,66,43,2])

# # for i in range(len(arr1)): 
# print(arr1[3])


# append method : 

print("question : 3 ")

my_array.append(7)

print(my_array)


print('Question : 4')


my_array.insert(0,101)
print(my_array)


print('Question : 5')

my_array1 = array('i',[10,11,12,13,14,15,10])
my_array.extend(my_array1)
print(my_array)


print('Question :6 its not comming from the array its from the list in , python the array and list is totally different !! You see !')

templist = [20,22,21]
my_array.fromlist(templist)

print(my_array) 


print('Step : 7')

my_array.remove(7) #it's non recursive if it finds the charecter first it will remove it from the first then it will hammpare it from the last 

print(my_array)

print('Question: 8')

my_array.pop() #it just poped from the last element : 
print(my_array)

print("Question no : 9 ")

#fetching any element from the array by using the index method 

my_array.index(10) #if you do this it will not print the index number of the element no you have to put that in the print section
print(my_array.index(10)) # see it's printing here with : 7 number of the index number now  

print('Question no : 10 ')

my_array.reverse()
print(my_array)

print('step ; 11')

print(my_array.buffer_info()) #it basically says our array buffer starts from this location and it has 15 elements 
# print(my_array)

print('step :12')
#it shows any duplicated or the elements that appears again and again in the array if you need to count them all : then you you count;
print(my_array.count(10))



