import numpy as np

# arr=np.array([[[10,20,30],[30,40,50]],[[60,70,80],[80,90,100]]])
# print(arr)
# print("\n",arr.shape)
#
# x=np.zeros((2,3,4))
# print("\n",x)
#
# x=arr.copy()
# print("\nCopy of array\n",x)
#
# x=arr.view()
# print("\n",x)
#
# arr[0]=110
# print("\n",arr)
#
# arr=np.array([10,20,30,40,50,60])
# result=arr.reshape(2,3)
# print("\n",result)
#
# arr=np.array([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160])
# print("\n",arr.reshape(2,2,4))
#
#
# arr=np.array([10,20,30,40,50,60],ndmin=2)
# print("\n",arr)

arr=np.array([[2,4,6],[8,10,12]])
for row in arr:
    print("\n",row)
    for x in row:
        print("\n",x)

print("---------------------")
arr=np.array([[[2,4,6],[8,10,12]],[[13,14,15],[16,17,18]]])
print("\n",arr)
for row in arr:
    print("\n",row)
    for x in row:
        print("\n",x)
        for y in x:
            print(y)

arr=np.array([[[2,4,6],[8,10,12]],[[13,14,15],[16,17,18]]])
print(arr.ravel())
print(arr.sum())
print(arr.sum(1))
print(arr.min())
print(arr.max())


a=np.array([[2,4,6],[8,10,12]])
b=np.array([[2,4,6],[8,10,12]])
print("\n",a+b)
print("\n",a-b)
print("\n",a*b)
print("\n",a**b)
print("\n",a/b)
print("\n",a//b)

x=a.dot(b.T)
print(x)

res = np.concatenate((a,b))
print("\n",res)

arr = np.arange(9)
print("\n",arr)

result=np.split(arr,3)
print(result)

a=np.array([[2,4,6],[8,10,12]])
print("\n",np.append(a,[[20,21,22]],axis=0))

a=np.array([[2,4,6],[8,10,12]])
print("\n",np.append(a,[[20,21,22],[24,25,26]],axis=0))
a=np.array([[2,4,6],[8,10,12]])
print("\n",np.append(a,[[20,21,22],[24,25,26]],axis=1))

print("\n",a)
print("\n",np.delete(a,5))
x=np.arange(12).reshape(4,3)
print("\n",x)
print("\n",np.flip(x))

g=np.argmax(x)
print("\n",g)

