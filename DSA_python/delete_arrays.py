import numpy as np

mynew_array = np.array([[81,82,83,84],[71,72,73,74],[61,62,63,64],[11,22,33,44]])
found = False
def deletearray(array,delNum): 
    for i in range(len(array)): 
        for j in range (len(array[0])):
            if array[i][j] == delNum: 
                array[i].pop(j)
                found = True
                break 
        if found : 
            break
        if not found: 
            print('sorry your number couldnt found in the array ')
        

print(deletearray(mynew_array,61))
        
