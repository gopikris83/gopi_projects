import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Login@01"
)

print("MySQL ", mydb)

# -----------
# Creating a Database

print("--------Show Databases---------")
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Login@01",
    database = "myfirstdb"
)
mycursor = mydb.cursor()
mycursor.execute("Show Tables")

for x in mycursor :
    print(x)

# Connecting a database
print("Connect to a database")

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Login@01",
    database = "myfirstdb"
)

# Creating a table

#print("Creating a table")

#import mysql.connector

#mydb = mysql.connector.connect(
#    host = "localhost",
#    user = "root",
#    passwd = "Login@01",
#    database = "myfirstdb"
#)

#mycursor = mydb.cursor()
#mycursor.execute("Create table Customers (name varchar(25), address varchar(255))")