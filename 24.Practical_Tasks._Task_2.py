import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("CREATE INDEX idx_employees_name ON employees(name)")

conn.commit()

cursor.close()
conn.close()




