import numpy as np

mynew_array = np.array([[81,82,83,84],[71,72,73,74],[61,62,63,64],[11,22,33,44]])

# def deletearray(array,delNum): 
#     arr_list = array.tolist()
#     found = False
#     for i in range(len(arr_list)): 
#         for j in range (len(arr_list[0])):
#             if arr_list[i][j] == delNum: 
#                 arr_list[i].pop(j)
#                 return np.array(arr_list)
        

# print(deletearray(mynew_array,61))
        
def deletearray(array, delNum): 
    arr_list = array.tolist()
    for i in range(len(arr_list)): 
        for j in range(len(arr_list[0])):
            if arr_list[i][j] == delNum: 
                arr_list[i].pop(j)
                return np.array(arr_list)
    print('Number not found')
    return array
print(deletearray(mynew_array ,61))