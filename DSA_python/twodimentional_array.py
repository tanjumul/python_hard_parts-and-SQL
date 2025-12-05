#two dimentional array needs like a[i][j]
#multidimentional array we will use numpy : 

import numpy as np 

# twoDarray = np.array([[11,14,13,15],[16,17,18,25],[31,34,33,35],[41,44,43,45]])
# print(twoDarray)

#adding two way in column and row way , 

"""In the adding of n number of colums in the multidimentioal array 
it is calculated as O(mn) and the same for n number of rows o(mn) here by adding one array to the mult
dimentional array the next to all arrays will be replaced or steped once """



# twoDarray = np.array([[11,14,13,15],[16,17,18,25],[31,34,33,35],[41,44,43,45]])
# print(twoDarray)

# newTwoDarray = np.insert(twoDarray,0,[[1,2,3,4]],axis=1)
# print(newTwoDarray)


#multidimentional array practice : 

import numpy as np 

my_new_array = np.array([[1,2,3,4,5,6],[11,21,31,41,51,61],[12,22,32,42,52,62],[14,24,34,44,54,64]])
print(my_new_array)

# my_second_array = np.append(my_new_array,[[10,10,10,10,10,10]],axis=0)
# print(my_second_array)

#accessing an element in a two dimentional array: 
def accessElements(array , rowIndex , columnIndex): 
    if rowIndex >= len(array) and columnIndex >= len(array[0]): 
        print('Error ahead')
    else: 
        print(array[rowIndex][columnIndex])
    
accessElements(my_new_array , 2,4)