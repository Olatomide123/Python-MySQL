import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Olatomide123#",
    database="testdb" # insert this line after step 1
)

mycursor = mydb.cursor()

""""
(1) First step: To create database
# The created database name is testdb

# mycursor.execute("CREATE DATABASE testdb") # save this first, then do mycursor.execute("SHOW DATABASES")


mycursor.execute("SHOW DATABASES")


for db in mycursor:  # ie for every database in my cursor
    print(db)        # print/show the created databases

"""

"""
(2) Next step is to create a table
# create table name students with two main fields name(which is a string) and age (which is an integer)

# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
"""

"""
(3) Step three; Populating our database and table
# To do this, first create sql formular

sqlFormula = "INSERT INTO students (name, age) VALUES(%s, %s)" # Note that (%s, %s) are place holders
student1 = ("Rachel", 22)

mycursor.execute(sqlFormula, student1) # This is insert the content of student1 into our table

mydb.commit() # This function is very important, this is used for making changes in our database or our table,
                # ie to make sure the chnages is seen in our database
"""

""""
(4) To insert more than one value into our table, let's say an array
sqlFormula = "INSERT INTO students (name, age) VALUES(%s, %s)" # Note that (%s, %s) are place holders
students = [("Bob", 12),
            ("Amanda", 32),
            ("Jacob", 21),
            ("Avi", 28),
            ("Michelle", 17),
            ("Mike", 17),]
mycursor.executemany(sqlFormula, students)
mydb.commit()
"""

"""
(5) Selecting and Getting data
mycursor.execute("SELECT * FROM students") # For selecting the wanted data

myresult = mycursor.fetchall() # This will get all of the data ie To get the wanted data

for row in myresult:
    print(row)
"""

""" 
(6) To select and get a specific column
mycursor.execute("SELECT age FROM students")
myresult = mycursor.fetchall()  # This will get all of the data ie To get the wanted data

for row in myresult:
    print(row)
"""

# (7) TO fetch just one value ie the first value, use myresult = mycursor.fetchone() on line 73

""" 
(8) Query Conditions with WHERE and Wildcards

#sql = "SELECT * FROM students WHERE age = 17"

sql = "SELECT * FROM students WHERE name = 'Amanda'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)
"""

"""# (9) To search for a phrase using wildcards
sql = "SELECT * FROM students WHERE name LIKE '%ac%'" # The % sign here is our wildcard character

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(result)
"""

"""# (10) Another approach to step 9 is
sql = "SELECT * FROM students WHERE name = %s"

mycursor.execute(sql, ("MIKE",))

myresult = mycursor.fetchall()
for result in myresult:
    print(result)
"""

"""
Updating Entries and Limiting Queries
sql = "UPDATE students SET age = 13 WHERE name = 'Bob'"

mycursor.execute(sql)

mydb.commit() # Remember that any change made to the database has to be committed
"""

"""
for limiting quesries

mycursor.execute("SELECT * FROM students LIMIT 3 OFFSET 3") # ie to get the first 5 values of our db

myresult = mycursor.fetchall()

for result in myresult:
    print(result)
"""

""" 
Ordering our Queries and Results
sql = "SELECT * FROM students  ORDER BY age DESC " # DESC stands for descending

mycursor.execute(sql)

myresult = mycursor.fetchall()

for r in myresult:
    print(r)
"""

"""# Delete Result and Drop Table

# For deleting results
sql = "DELETE FROM students where age = 17"

mycursor.execute(sql)

mydb.commit()

# for deleting tables
sql = "DROP TABLE IF EXITS students"

mycursor.execute(sql)

mydb.commit()
"""
