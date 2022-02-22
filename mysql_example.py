import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
def connect_to_db():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

connection = connect_to_db() #call ?the function like so MP21/2/22   
# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor() #allows me to act on a database

# Execute SQL query
cursor.execute('SELECT * FROM products')

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
    print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')##adjust this code and use it to display in terminal a table

# Can alternatively get one result at a time with the below code
# while True:
#     row = cursor.fetchone()
#     if row == None:
#         break
#     print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')

# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()