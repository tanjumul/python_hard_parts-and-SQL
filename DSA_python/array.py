#multiple dimentions of arrays : 

# #array should be homogenious
# import array 

# my_array = array.array('i',[1,2,3,4,5,3]) #-------> o(n)  #for empty arry both the time and space complexity is to be constant and it have to be 0(1)
# print(my_array)


# import numpy as np 
# np_array = np.array([], dtype = int) #-------> o(1)
# print(np_array)

# np_array1 = np.array([1,2,3,4,5,56,7,8,4,2])
# print(np_array1)


#insersion into array : 

#inserting in the begining to the array: 

from array import *

# my_array1 = array.array('i',[1,2,3,4,5,6])
# print(my_array1)
#
# arr1 = array('i',[11,44,55,66,77,88,55,43,221,45])
#inserting now ; 
# my_array1.insert(0,10) #inserting at the (position , value) 

# print(my_array1)

#traversal of an array 


# def traversal_array(array): 
#     for i in array: 
#         print(i)
    
# traversal_array(arr1)



# from array import * 

# arr12 = array('i', [1,34,55,223,44])


# def perform_array(array): 
#     for i in array:
#         print(i)
# perform_array(arr12)


#another way if i want to create a function that will create an array then i will initialize the elements 


# def processing(elementss, typed = 'i'): 
    
#     arr = array(typed,elementss)
    
#     for ii in arr : #--(n)--> o
#         print(ii) #------>O(1)  and it is the space complexity too o(1)
#         #the time comppexity will be o(n)
    
#     return arr

# my_elements = processing([12,44,22,12])

# def processment(ele , typed = 'i'): 
#     arr = array(typed,ele)
#     for ii in arr: 
#         print(ii)
#     return arr 
# my_ele = processment([1,3,2,14,22])
## now if i want to access each elelment and i will create a funciton : 


# arr13 = array('i',[11,22,33,44,55,66,7])

# def find_array_num(array, index): 
#     if index > len(array):
#         print('Here is no such array num what you are giving index number')
        
#     else: 
#         print(array[index])

# find_array_num(arr13,int(input('your array number :')))


#searching for element : by linear search : 
import array 

#time complexity of linear search is o(n)
my_array1 = array.array('i',[1,3,4,56,7,54,32,2])

def linear_search(arr,target): #----> o(n)
    for i in range(len(arr)): 
        if arr[i] == target:  #----- o(1)
            return arr[target]   #----- o(1)
    else : 
            return -1   #----- o(1)
print(linear_search(my_array1, 3 ))     #----- o(1)