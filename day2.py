# a=100
# b=5
# add=a+b
# sub=a-b
# mul=a*b
# div=a/b
# mod=a%b
# exp=a**b
# if a % 2 == 0 :
#     print("even")
# else:
#     print("odd")
#
# if a % 2 == 0:
#     print("number is even")
#     if a % 10 == 0:
#         pass
#     else:
#         print("odd")
# print(add)
# print(sub)
# print(mul)
# print(div)
# print(mod)
# print(exp)
# print(bin(a))
# print(bin(b))
# print(a & b)


# per= int(input("percentage : "))
# if per > 60:
#     print("grade A")
# elif per >60 and per<50:
#         print("grade B")
# else: print("grade c")

#calculator

# a=int(input("enter a value : "))
# b=int(input("enter a value : "))

# c = str(input("enter the function : "))
# if c == '+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c == '*':
#     print(a*b)
# elif c=='/':
#     print(a/b)
# else: print("false")

#loops

# for x in range(1,10,1):
#     print(x)

# n1= int(input("num = "))
# for x in range(1,11,1):
#     print(n1,"*",x,"=",n1*x)

# for x in range(1,11,1):
#     if x%2== 0:
#         continue
#     print(n1,"*",x,"=",n1*x)


# for x in range(2,5):
#     for y in range(1,11):
#         print(x,"*",y,"=",x*y)

# for x in range(0,10,1):
#     for y in range(1,x,1):
#         print(y,end=" ")
#     print()

# i=1
# while (i<10):
#     print(i)
#     i +=1

# while True:
#     n= int(input("enter any number and 0 exit : "))
#     if n == 0:
#         break
#     print(n)

# str="Python Program"
# print(str[2])
# str="Python Program"
# print(str[-2])
#
# str="Python Program"
# print(str[0:4])
#
# str="Python Program"
# print(str[0::4])
#
# str="Python Program"
# print(str[-1::-1])
#
# str="Python Program"
# l=len(str)
# print(l)
# for x in range(l):
#     print(str[x])
#
# print(ord("a"))
# print(chr(97))
#
# l=[10,20,30,40,50,"python"]
# print(l)
#
# l=[10,20,30,40,50]
# print(type(l))
#
# l=[10,20,30,40,50,[10,20,30]]
# print(l[5][2])
# print(l[-1])

l=[]
l.append(10)
l.append(20)
l.append(50)
l.insert(1,39)
l.remove(39)
l.pop()
print(l)
