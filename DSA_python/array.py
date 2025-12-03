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
arr1 = array('i',[11,44,55,66,77,88,55,43,221,45])
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


def processing(elementss, typed = 'i'): 
    
    arr = array(typed,elementss)
    
    for ii in arr : 
        print(ii)
    
    return arr

my_elements = processing([12,44,22,12])