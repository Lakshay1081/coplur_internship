import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

# arr=np.array([10,20,30,40,50])
# print(arr[1])
#
# arr[0],arr[1]=arr[1],arr[0]
# print(arr)
#
# arr=np.array([[10,20,30,40,50],[60,70,80,90,100]])
# print(arr)
# # print(arr[0,3])
# # arr[0,3]=arr[1,2]
# # print(arr)
# # arr[0,3],arr[1,2]=arr[1,2],arr[0,3]
# # print("after swapping\n",arr)
#
# arr[[0,1],:]=arr[[1,0],:]
# print("row swapping\n",arr)
# arr[:,[0,1]]=arr[:,[1,0]]
# print("column swapping\n",arr)
# arr=np.array([[[10,20,30,40,50],[60,70,80,90,100]],[[1,2,3,4,5],[6,7,8,9,10]]])
# print("\n",arr)
#
# # arr[0,0,2],arr[1,0,2]=arr[1,0,2],arr[0,0,2]
# # print("after swapping\n",arr)
#
# arr[[0,1],:,:]=arr[[1,0],:,:]
# print("row swapping\n",arr)
#
# arr[[0,1],[0,1],:]=arr[[1,0],[1,0],:] #idhar pehla bracket set ke liye h , agla bracket rows ka h
# print("specific 0000000row swapping\n",arr)
#
# arr[:,:,[0,1]]=arr[:,:,[1,0]]
# print("column swapping\n",arr)

# arr=np.array([1,2,np.nan,4,5])
# print(arr)
# emp= np.isnan(arr)
# print(emp)
#
# print("\n",np.nan_to_num(arr,copy=True,nan=0.0,posinf=None,neginf=None))

# a=np.array([[1,2,3],[4,5,6]])
# np.save('data.npy',a)
#
# res= np.load('data.npy')
# print(res)
#
# a1=np.array([[1,2,3],[4,5,6]])
# a2=np.array([1,2,3])
# np.savez('data.npz',array1=a1,array2=a2)
# res= np.load('data.npz')
# print("\n",res)
# print("\n",res['array1'])
# print("\n",res['array2'])

# with open('data.txt','w') as f:
#     f.write("1.0 2.0 3.0\n4.0 5.0 6.0\n7.0 8.0 9.0")
# res =np.loadtxt('data.txt')
# print(res)
#
# data=np.array([[2.0,3.0,4.0],[5.0,6.0,7.0]])
# np.savetxt("output.txt",data,delimiter=' ',fmt='%1.1f')
# res=np.loadtxt("output.txt")
# print("\n",res)
#
# with open('data.csv','w') as f:
#     f.write("1.0,2.0,3.0\n4.0,5.0,6.0\n7.0,8.0,9.0")
# data=np.genfromtxt('data.csv',delimiter=',')
# print("csv ka output\n",data)
#
# a1=np.array([[1,2],[3,4]])
# a2=np.array([5,6])
# res=np.linalg.solve(a1,a2)
# print("\n",res)
#
# a1=np.array([[1,2],[3,4]])
# a2=np.array([5,6])
#
# a1_inv=np.linalg.inv(a1)
# print("\n",a1_inv)
#
# res=np.dot(a1_inv,a2)
# print("\n",res)

# x=np.linspace(0,10,100)
# y=np.sin(x) #sin value calculation
# print(y)

# plt.plot(x,y,label='sin(x)',color='red',linestyle='--')
# plt.title("line plot of sin(x)")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
#
# plt.legend()
#
# plt.grid(True)
# plt.show()

# categories=['A','B','C','D']
# value=[1,2,3,4]
# plt.bar(categories,value,color='red')
# plt.show()

categories=['A','B','C','D']
value=[1,2,3,4]
plt.pie(value,labels=categories,autopct='%1.1f',startangle=140)
plt.show()