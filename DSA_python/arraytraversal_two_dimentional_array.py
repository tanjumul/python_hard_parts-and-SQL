import numpy as np 

my_new_array = np.array([[1,2,3,4,5,6],[11,21,31,41,51,61],[12,22,32,42,52,62],[14,24,34,44,54,64]])

# def traversal_array(array): 
#     for i in range(len(array)): 
#         for j in range(len(array[0])): 
#             print(array[i][j])
# traversal_array(my_new_array)

    
    
    
    
def traverserTA(array):
    for i in range(len(array)): 
        for j in range(len(array[0])):
            print(array[i][j])

traverserTA(my_new_array)