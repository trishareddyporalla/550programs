import sqlite3

# Connect to the database
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()
# Uncomment these lines if you need to create the table and insert records for the first time
# cur.execute("""CREATE TABLE IF NOT EXISTS students (name VARCHAR, roll_no VARCHAR, section VARCHAR)""")
# cur.execute('INSERT INTO students VALUES ("pradeep", "501", "A")')
# cur.execute('INSERT INTO students VALUES ("srikanth", "502", "B")')
cur.execute('INSERT INTO students VALUES ("shekar", "503", "C")')

# Update a specific record
cur.execute('UPDATE students SET name = "pradeep" WHERE roll_no = "501"')

# Commit the transaction
con.commit()

# Fetch and print all records to verify the update
cur.execute('SELECT * FROM students')
rows = cur.fetchall()
print(rows)

# Optional: Print all table names
# cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cur.fetchall()
# print(tables)

# Close the connection
con.close()
