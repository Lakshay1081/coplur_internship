""" Create a CSV file for address book, CSV file should have column for name, address, mobile, email. Insert 2-3 dummy data"""
import csv

data=[["Name","Address","Mobile","Email"],
      ["ABC","Jaipur",9876543210,"abc@example.com"],
      ["DEF","Delhi",9630258147,"def@example.com"],
      ["GHI","Jaipur",7418529630,"ghi@example.com"]]
with open("address_book.csv",'w',newline="") as file :
    writer=csv.writer(file)
    for row in data :
        writer.writerow(row)

with open('address_book.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


""" Refer to our example of weather data and get more details. Display them """
import requests

def weather_details(city, api_key):
    final_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(final_url)
        response.raise_for_status()
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"].capitalize()
        pressure = data["main"]["pressure"]
        grnd_level = data["main"]["grnd_level"]
        speed = data["wind"]["speed"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C (Feels like: {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Pressure: {pressure}")
        print(f"Ground level: {grnd_level}")
        print(f"Wind Speed: {speed}")


    except requests.exceptions.RequestException as a:
        print(f"Error fetching weather data: {a}")

api_key = "193354bd588c02626a0f569688308bc9"
city = input("Enter city name: ")

weather_details(city, api_key)



""" Create Database,Create 2-3 tables,Insert some records,Perform different select operations,Update some data,Delete some data """
import sqlite3

conn = sqlite3.connect("college.db")


conn.execute("""
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

conn.execute("""
CREATE TABLE Courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    duration TEXT
)
""")

#inserting data in student table
conn.execute("INSERT INTO Students (name, age, city) VALUES ('lakshay', 20, 'Jaipur')")
conn.execute("INSERT INTO Students (name, age, city) VALUES ('shivam', 22, 'Delhi')")
conn.execute("INSERT INTO Students (name, age, city) VALUES ('suchitra', 21, 'Mumbai')")

#inserting data in courses table
conn.execute("INSERT INTO Courses (course_name, duration) VALUES ('Python Programming', '3 months')")
conn.execute("INSERT INTO Courses (course_name, duration) VALUES ('Data Structures', '2 months')")

#using Select Operations
print("\nAll Students:")
data=conn.execute("SELECT * FROM Students")
for row in data:
    print(row)

print("\nStudents from Jaipur:")
data=conn.execute("SELECT * FROM Students WHERE city = 'Jaipur'")
for row in data:
    print(row)

print("\nAll Courses:")
data=conn.execute("SELECT * FROM Courses")
for row in data:
    print(row)

#Updating Record
conn.execute("UPDATE Students SET city = 'Bangalore' WHERE name = 'suchitra'")

#updated data
print("\nAfter Update:")
data=conn.execute("SELECT * FROM Students")
for row in data:
    print(row)

# Deleting a Record
conn.execute("DELETE FROM Students WHERE name = 'lakshay'")

print("\nAfter Deletion:")
data=conn.execute("SELECT * FROM Students")
for row in data:
    print(row)

conn.commit()
conn.close()
