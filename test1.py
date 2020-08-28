import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Olatomide123#",
    database="testdb"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM students WHERE name LIKE '%ac%'" # The % sign here is our wildcard character

mycursor.execute(sql)

myresult = mycursor.fetchall()

for result in myresult:
    print(myresult)


