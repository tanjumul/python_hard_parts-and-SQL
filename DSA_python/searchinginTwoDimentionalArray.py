
import numpy as np 


my_new_array = np.array ([[1,2,3,4,5,6],
                         [11,21,31,41,51,61],
                         [12,22,32,42,52,62],
                         [14,24,34,44,54,64]])



def serarching(array,value): 
        for i in range(len(array)):
             for j in range(len(array[0])): 
                 if array[i][j] == value: 
                     return f'value is located in the {i} {j} and the value you are looking {value}'
        else: 
                      
                      return 'The number you are looking here in the array doesnt exitst'
                      
print(serarching(my_new_array,51))