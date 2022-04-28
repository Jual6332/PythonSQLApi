import sqlite3

# Connecting to the database
db_connection = sqlite3.connect('clientdata.db')
print("Connected to the database")
crsr = db_connection.cursor() # Cursor acts as middleware to execute SQL queries for us

# Create Table of employee information
create_employee_table = """CREATE TABLE employee_information (
employee_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
job_title VARCHAR(30),
salary INTEGER);"""

# SQL Query: Create Table in SQL
crsr.execute(create_employee_table)
print("Created Employee table.")

# Add Employee Data
add_employee_data1 = """INSERT INTO employee_information VALUES 
(1,"John","Smith","Supervisor I",72000);"""
add_employee_data2 = """INSERT INTO employee_information VALUES 
(2,"Winston","Jones","Supervisor I",72000);"""

# SQL Query: Write Employee Data to the Database
crsr.execute(add_employee_data1) # Add employee1 data
crsr.execute(add_employee_data2) # Add employee2 data
print("Added Employee data.")

# Save changes to the database
db_connection.commit()

# Fetch all stored data
crsr.execute("SELECT * FROM employee_information")
employee_information = crsr.fetchall()

# Print the fetched employee data
crsr.execute(add_employee_data1) # Add employee1 data

# Close the database connection
db_connection.close()
