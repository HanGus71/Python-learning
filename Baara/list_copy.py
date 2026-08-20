list=['b','m','g']
list_copy=list.copy()
#print(list)
#print(list_copy)
import copy
matrix=[
    ['a','b','c'],
    ['d','e','f']
]   
matrix_copy = copy.deepcopy(matrix)
print(matrix)
print(matrix_copy)