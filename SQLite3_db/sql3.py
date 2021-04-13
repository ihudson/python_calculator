#################################
# Connect to sqlite3 database
# Ian Hudson
# Date: 02/22/2021
#################################
# Clear Terminal Screem

import sqlite3
import os
os.system('clear')

###########################
# SQLite Database
###########################
# Connect to the database

conn = sqlite3.connect('customer.db')
#Create a cursor()
c = conn.cursor()

# Create Table
# c.execute("INSERT INTO customer VALUES('Ian','Hudson','ihudson709@hotmail.com')")

c.execute("SELECT * FROM customer")

print(c.fetchall()[0])



'''
c.execute("""CREATE TABLE customer (
            first_name text,
            last_name text,
            email text
            )""")
'''

#Commit changes
conn.commit()







# Close Datbase connection
conn.close()
