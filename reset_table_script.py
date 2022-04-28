import sqlite3

# Connecting to the database
db_connection = sqlite3.connect('clientdata.db')
print("Connected to the database")
crsr = db_connection.cursor() # Cursor acts as middleware to execute SQL queries for us

# Drop table (which table?)
sql_query = """(DROP TABLE employee_information);"""
db_connection.execute(sql_query)

# Close connection to the database
db_connection.close()
