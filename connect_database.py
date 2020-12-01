import sqlite3 
  
# connecting to the database  
connection = sqlite3.connect("myTable.db") 
  
# cursor  
crsr = connection.cursor() 
  
# SQL command to delete a table
sql_command = """Drop TABLE building;"""
  
# execute the statement 
crsr.execute(sql_command) 

# SQL command to create a table in the database 
sql_command = """CREATE TABLE building (  
name VARCHAR(20) PRIMARY KEY,  
people INTEGER );"""
  
# execute the statement 
crsr.execute(sql_command) 
  
# SQL command to insert the data in the table 
sql_command = """INSERT INTO building VALUES ("West", 10);"""
crsr.execute(sql_command) 
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 

connection.close() 