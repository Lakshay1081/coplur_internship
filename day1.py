str1=input("enter string 1 : ")
str2=input("enter string 2 : ")

concat_str= str1 + str2
print("concatinated string is : ", concat_str)

print("hello world" , "welcome",6,sep=" - ", end="---")
print("lakshay" ,end="---")
print("Pareek")
#sep line ke beech mein space ko fill karne ke kaam aata h
#end next line ko usse pehli waali line mein join karega
print(10>5)
a=4
b=7
print("the sum of " ,a ,"and",b,"is",a+b,sep="--")
print("the product of " ,a ,"and",b,"is",a*b)

print(f"the sum of {a} and {b} is", {a+b},sep="--")
#f is formatting and string formatting
print(f"the value of {22/7:.2f}")

#name=input("enter your name =")
#print("your name is = ",name)

#a= int(input("value of a is = "))
#b=int(input("value of b is = "))
#print("the sum of a and b is ",a*b)

#help("keywords")

#a=10
#b=6
#print(id(a))

name="lakshay"
print(name.upper())
print(name.lower())
print(name.count("k"))
print(name.expandtabs(4))

c="--"
seq=("a","b","c")
print(c.join(seq))

l="tipon"
e="71633"
str="my name is lakshay"
encoding = str.maketrans(l,e)
print(str.translate(encoding))