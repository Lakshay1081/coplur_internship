"""Write a python program that takes in a student name, class.
It should also take in five subject marks of the students and find the total mark and percentage.
Display a result in such a way that their name, class,  and percentage are printed."""

name=input("enter student name : ")
student_class=input("enter class : ")

print("enter your marks")
MATHS = float(input("enter MATHS marks : "))
DSA = float(input("enter DSA marks : "))
JAVA = float(input("enter JAVA marks : "))
PYTHON = float(input("enter PYTHON marks : "))
DBMS = float(input("enter DBMS marks : "))

total_marks = MATHS + DSA + JAVA + PYTHON + DBMS
percentage = (total_marks/500) * 100


print("\nname : ",name)
print("class : ",student_class)
print("total marks : ",total_marks)
print(f"percentage : {percentage:.2f}%")
if percentage>=90:
    print("Grade A++")
elif percentage>=80 and percentage<90:
    print("Grade A+")
else: print("Grade A")

"""Input 2 strings concatinate them and store in another variable. 
then perform generally used string methods on it"""

str1=input("\nenter string 1 : ")
str2=input("enter string 2 : ")

concat_str= str1 + str2
print("concatinated string is : ", concat_str)
print("Uppercase : ",concat_str.upper())
print("Lowercase : ",concat_str.lower())
print("Count : ",concat_str.count("a"))
print("the concatenated string of",str1,"and",str2,"is",str1+str2,sep="--")
l="lakshay"
e="1234567"
encoding= concat_str.maketrans(l,e)
print(concat_str.translate(encoding))
print("length : ",len(concat_str))
print("capatalize : ",concat_str.capitalize())
print("Startwith : ",concat_str.startswith("h"))
print("Endswith : ",concat_str.endswith("h"))
print("Split : ",concat_str.split(" "))
print("Find",concat_str.find("s"))
print("rFind",concat_str.rfind("s"))


