
import numpy as np 


my_new_array = np.array ([[1,2,3,4,5,6],
                         [11,21,31,41,51,61],
                         [12,22,32,42,52,62],
                         [14,24,34,44,54,64]])



def serarching(array,value): 
        for i in range(len(array)):#---------> this has the complexity of o(mn)
             for j in range(len(array[0])): #------------> this has the complexity of o(n)
                 if array[i][j] == value: #----------------> this has the complexity of o(1)
                     return f'value is located in the {i} {j} and the value you are looking {value}' #o(1)
        else: 
                      
                      return 'The number you are looking here in the array doesnt exitst' #--->O(1)
                      
print(serarching(my_new_array,51))

#starting the day with DSA Postgres & FastApi