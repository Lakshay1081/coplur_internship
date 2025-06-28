import numpy as np
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(type(a))
# print(a.dtype)
#
# arr=np.array([56,48,57,89],dtype='S')
# arr=np.array([56,48,57],dtype='i8')
# # arr=np.array([]).dtype
# print(arr)
# print(arr.dtype)
#
# arr=np.zeros(5)
# print("\n",arr)
# arr=np.ones(5)
# print("\n",arr)
# arr=np.ones((2,3),order='F')
# print("\n",arr)
# arr=np.ones(((2,3,4)))
# print("\n",arr)
# arr=np.arange(10) #default 0 se start karta h
# print("\n",arr)
# arr=np.arange(1,10,2)
# print("\n",arr)
# arr=np.linspace(0,5,num=5)
# print("\n",arr)
# arr=np.linspace(0,5,num=5,endpoint=True)
# print("\n",arr)
# arr=np.linspace(0,5,num=5,endpoint=False)
# print("\n",arr)
# arr=np.linspace(0,5,num=5,retstep=True)
# print("\n",arr)
# arr=np.linspace(0,5,num=5,retstep=False)
# print("\n",arr)
#
# arr=np.random.rand(2,3)
# print(arr)

# arr=np.empty((2,3))
# print("\n",arr)
# arr=np.full((2,3),5) #we give values to make a array
# print("\n",arr)

arr=np.array([23,55,89,58,63])
print("\n",arr)
print("\n",arr[::2])
print("\n",arr.sum())
print("\n",arr[1]+arr[2])
arr=np.array([[[25,56,44,14,42],[78,98,95,25,56]],[[45,89,86,85,96],[78,89,48,56,86]]])
print("\n",arr)
print("\n",arr[0,1,2])
print("\n",arr[1,1,2:4])
arr=np.array([[25,56,44,14,42],[78,98,95,25,56]])
print("\n",arr)
print("\n",arr[0,1])
print("\n",arr[1,1:4])





