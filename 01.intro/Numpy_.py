import numpy as np 
arr1=np.array([1,2,3,4,5])  # 1D array 
arr2=np.array([[4,5,6],[1,9,10]]) # 2D array 
arr3=np.array([[14,5,61],[13,29,51],[11,78,90]])
arr4=np.arange(1,50,2)  
arr5=np.arange(51,100,2)
arr6=np.linspace(1,10,4)
arr7=np.zeros(3,dtype=int)    # o's array
arr8=np.ones((1,2),dtype=bool)  #1's array
arr9=np.full((3,3),3.5)     # array of arbitary number(eg-3.5)
np.random.seed(2)  # this maintains same sequence while genarating random numbers
arr10=np.random.rand(3,4)  # random array of floating values of 3 rows and 4 columns 
arr11=np.random.randint(1,10,(2,2)) # random array between 1 and 10 integers with 2 rows and 2 columns
#methods 
print(arr1.shape)   # gives rows and columns
print(arr1.size)    #gives total no.of elements
print(arr1.dtype)   #gives datatype of elements
print(arr1.ndim)    #gives dimension of array
print(arr2.reshape(6,1)) # reshaping array
#accessing 
print(arr1[2])    # output-3
print(arr2[1][2])   # output-10
print(arr2[:,0])  # output-[4,1]
# arithmetic operations 
print(arr1+2)  # adds 2 to every element of arr1 (-,*,/,%,//,**)
print(arr4+arr5)   # adding two same dimensions arrays (-,*,/,%,//,**)
print(arr3.min())   # minimum of array3
print(arr3.max())   # maximum of array3
print(arr3.sum())   # sum of all elements in array3
print(arr3.mean())  # mean of all ele in array3
print(arr3.std())  # standard deviation of all ele in array3
print(np.sin(arr1)) # trigonometry functions  on all ele of  array3  (cos,tan etc.)
print(np.dot(arr2,arr3))  # matrix multiplication of arrays 
