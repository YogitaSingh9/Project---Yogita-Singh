import sqlite3
conn= sqlite3.connect('ecommerce.db')
cursor=conn.cursor()
print("table schema")
cursor.execute('PRAGMA table_info(products)')
for row in cursor.fetchall():
    print(row)
print("\nSample data from products table:")
cursor.execute('SELECT * FROM products LIMIT 5')

for row in cursor.fetchall():
    print(row)
conn.close()