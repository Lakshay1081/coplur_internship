# d={1:"lakshay",2:"shivam",3:"suchitra"}
# print(d)
#
# d={1:"lakshay",2:"shivam",3:"suchitra"}
# print(d[1])
#
# d={1:"lakshay",2:"shivam",3:"suchitra",4:{1:"one",2:"two"}}
# print(d[4][1])
#
# dict={}
# print(dict)
# dict[0]="pyhton"
# dict[1]="python"
# dict[2]="DBMS"
# # dict.pop(1)
# print(dict)
# # del(dict[2])
# # print(dict)
# dict2={3:"maths",4:"TOC"}
# print("dict2 : ",dict2)
# # dict.clear()
# # print(dict)
# print(dict.get(2))
# print(dict.items())
# # print(dict.popitem())
#
# dict2.update(dict)
# print(dict2)
#

"""tuple"""
# from itertools import count
#
# t=(10,20,30,40,50,30,20)
# print(t)
# print(type(t))
#
# l=len(t)
# for x in range(7):
#     # print(x,t[x])
#     print(t[1])
#
# t4=("xyz",)*3
# print(t4)
# l=[10,20,30,40,50]
# t=(tuple(l))
# print(t)
# print(min(t))
# print(max(t))
# print(t.count(10))
#
# s={"a","b","c","d"}
# print(s)
# s.add("e")
# print(s)
#
# s2={"apple","pineapple","grapes"}
# s3=s.union(s2)
# print(s3)
#
# s5=set()
# s6=set()
# for i in range(5):
#     s5.add(i)
# for i in range(3,9):
#     s6.add(i)
#     s7=s5.intersection(s6)
#     print(s7)
#     s8=s5 & s6
#     print(s8)

def my_name():
    print("python")
my_name()

def add(a,b):
    print("addition of a and b is =",a+b)
    res=a+b
    return res
add(12,15)

def place(city1,city2,city3):
    print("the first city is : " + city1)

place(city1="a",city2="b",city3="c")

def place(**city):
    print(city['snm'])
place(fnm='a',snm='b',gnm='c')

def place(*city):
    print(city[2])
place("a","b","c")

f= open("new1.txt","w")
f.write("this is first line\n")
f.close()

f= open("new1.txt","r")
for x in f:
    print(x)

f=open("new1.txt","r")
print(f.read())

with open("new1.txt") as file:
    data=file.read()
    print(data)

with open("new1.txt") as file:
    data=file.readlines()
    for line in data:
        word= line.split()
        print(word)