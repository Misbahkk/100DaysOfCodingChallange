orignal_list = [[1,2,3],[4,5,6]]

# shallow copy 
print("This is orignal copy: ",orignal_list)
shallow_copy = orignal_list.copy()
print(shallow_copy)

shallow_copy[0][0] = 10
print(orignal_list)

# deep coopy
import copy
deep_copy = copy.deepcopy(orignal_list)
print("This is deep copy: ",deep_copy)

deep_copy[0][0] = 5
print("This is orignal copy after modify deep copy: ",orignal_list)
print("This is deep copy after modify deep copy: ",deep_copy)
