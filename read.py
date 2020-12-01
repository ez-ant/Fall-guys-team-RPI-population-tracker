import sqlite3 
  
# connecting to the database  
connection = sqlite3.connect("myTable.db") 
  
# cursor  
crsr = connection.cursor() 
  
  
# SQL command to insert the data in the table 
sql_command = """Select name, people from building;"""
crsr.execute(sql_command) 
result = crsr.fetchall()

connection.close() 
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
print(result)