"""In your last program where you find the total and percentage of a student's marks of 5 subject,
find the grade of the student using conditional statement.
Eg. grade 'A' if percentage is greator than or equals to 60,
'B' for  percentage is greator than or equals to 50 and less than 60,
'C' for  percentage is greator than or equals to 40 and less than 50,
'D' for  percentage is greator than or equals to 33 and less than 40, otherwise 'Fail'"""

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
if percentage>=60:
    print("Grade A")
elif percentage>=50 and percentage<60:
    print("Grade B")
elif percentage >= 40 and percentage < 50:
    print("Grade C")
elif percentage >= 33 and percentage < 40:
    print("GradeDB")
else: print("FAIL")


"""Input a number from user and find its factorial using for loop"""

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")

""" Create a billing program using list. Program should have options to 
1. Create Bill
2. Display Item Price and total bill amount
3. Display Total
4. Exit """


c=[]
while True:
    print('''
    1. Create Bill
    2. Display Item Prices and Total Bill Amount
    3. Display Total
    4. Exit
    ''')

    ch = int(input("Enter choice (1-4): "))
    if ch == 1:
        while True:
            item = int(input("Enter price of item (0 to exit): "))
            if item == 0:
                break
            c.append(item)
            print(c)

    elif ch == 2:
        total = 0
        print("Item Prices list :", c)
        for m in c:
            total += m
        print("Total bill amount is:", total)

    elif ch == 3:
        total = 0
        for m in c:
            total += m
        print("Total bill amount is:", total)

    elif ch == 4:
        print("Exit")
        break

    else:
        print("Invalid choice!")

"""Write a  Python program to find the smallest number in a list."""

a= [5, 2, 9, 1, 7]

smallest = a[0]
for x in a:
    if  x < smallest:
        smallest = x

print("Smallest number is:",smallest)


"""Write a  Python program to find the second greatest number in a list."""

"""Write a  Python program to find the second smallest number in a list."""

a= [5, 2, 9, 1, 7]

smallest = a[0]
greatest = a[0]
smallest2= a[0]
greatest2= a[0]
for x in a:
    if  x < smallest:
        smallest = x

print("Smallest number is:",smallest)

for y in a:
    if y < smallest2:
        if y > smallest:
            smallest2 = y

print("2nd smallest is : ", smallest2)

for w in a:
    if  w > greatest:
        greatest = w

for z in a:
    if z > greatest2:
        if z <greatest:
            greatest2 = z

print("2nd smallest is:",greatest2)


