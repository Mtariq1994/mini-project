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