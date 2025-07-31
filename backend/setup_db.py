import sqlite3
conn= sqlite3.connect('ecommerce.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, cost REAL, category TEXT, name TEXT, brand TEXT,retail_price REAL, department TEXT, sku TEXT, distribution_center_id INTEGER)''')
conn.commit()
conn.close()