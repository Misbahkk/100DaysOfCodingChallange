import numpy as np
#Vector
ex_my = [1,2,3,4,5]
print(ex_my , 5)
x = np.array(ex_my)
print(x)
y = type(x)
print(y)
print(x.ndim)    # this shows how many dimensions the array has
print(x.shape)   # this shows the shape

#________________________________________
#Matrix
arr1 = [2,4,6]
arr2= [1,3,5]
my_list = [arr1,arr2]
print(my_list)
my_matrix = np.array(my_list)
print("\n\nThis is a matrix \n",my_matrix)
my_tranpose = my_matrix.transpose()
print("\nThis is a transpose \n",my_tranpose)
print(my_tranpose.ndim)

#______________________________________________________________
#arange() function is used 
# np.arange(start value , end value, step size , dtype = "type")

ex_arrange = np.arange(0,11,2)
print("\n\n Arrange function \n",ex_arrange)

 #Creating arrays of evenly spaced points with linspace()
 #np.linspace(start value, end value, number of points)

ex_linespace = np.linspace(0,10,5)
print("\n\nLinespace() functio \n",ex_linespace)
#___________________________________________________________
# Example 58: creating arrays with unique elements.
# Let us use the zeros () function to create a vector and a matrix.
zero_1= np.zeros(3)
zero_2 = np.zeros((2,3))
print("\n\n Zeros  vector \n", zero_1 ,"\n\n zeros matrix \n" , zero_2)
#_________________________________________________________________
#Let us use the ones () function to create a vector and a matrix
ones_1 = np.ones(3)
ones_2 = np.ones((2,3))
print("\n\n ones vector \n", ones_1 ,"\n\n Ones matrix \n" , ones_2)
#______________________________________________-
#Let us use the eye () function to create matrix
eye_1 = np.eye(2)  # A matrix of 4 elements 2 rows, 2 columns
eye_2 = np.eye(3) #3colum and 3 row
print("\n\n eye 2 row and 2 colums matrix \n", eye_1 ,"\n\n eye 3 row and 3 columns \n" , eye_2)

#____________________________________________________________________
#Example 59: Generating arrays with random values
#_____________________________________________________
#rand() funtion genrate the random numbers between 0 and 1

rand_1 = np.random.rand(2) # 1 dimentional arry
rand_2 = np.random.rand(2,3) # 2 dimentinaol 6 elemwnts
print("\n\n rand() funtion genrate the random numbers between 0 and 1")
print(rand_1 ,"\n" , rand_2)
#_____________________________________________________
#randn() funtion genrate the random numbers arround zero also inculde - value 

randn_1 = np.random.randn(2) # 1 dimentional arry
randn_2 = np.random.randn(2,3) # 2 dimentinaol 6 elemwnts
print("\n\n randn() funtion genrate the random numbers arround zero")
print(randn_1 ,"\n" , randn_2)
#_____________________________________________________
#Random() --> Syntax: np.random(lower value, higher value, number of values, dtype)
random_1 = np.random.randint(1,5) # genrate random number between 1 to 5 only 1 number select
random_2 = np.random.randint(1,100,10) # genrate 6 random numbers between 1 to 100
random_3 = np.random.randint(1,100,(2,3)) # genrate 2 dimentional arry 2 rows and 3 colum and numbers are random
print("\n\n " , random_1 ,"\n",random_2,'\n',random_3) 

#___________________________________________________________________________________
#___________________________________________________________________________________
# MANIPULATING ARRAYS 
# Example 60 : Using the reshape() method
# Let us declare a few arrays and call the reshape method to change their dimensions.
shape1 = np.arange(10)
shape2= np.random.randint(20,50,10)
print("\nshape1\n",shape1,'\nshape2\n',shape2)
reshape_ex1 = np.reshape(shape1,(5,2))
reshape_ex2 = np.reshape(shape2,(2,5))
print("\nreshape_ex1\n",reshape_ex1,'\nReshape_ex2\n',reshape_ex2)

#___________________________________________________________________________________
#___________________________________________________________________________________
# we can use the .max( ) , .min( ) ,
#  .argmax( ) and .argmin( ) methods respectively
# Example 61:
#  Let us find the maximum and minimum values in the ‘values’ array, along
#  with the index of the minimum and maximum within the array.
A = shape2.max()
B = shape2.min()
C = shape2.argmax()
D = shape2.argmin()
print(f'Maximum value in Shape2 is: {A} \n Minimum Value in shape2 is: {B} \n Maximum value iteam no is: {C}\n Minimum value iteam number is: {D}')



