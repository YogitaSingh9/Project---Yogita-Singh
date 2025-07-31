import sqlite3
import csv
conn=sqlite3.connect('ecommerce.db')
cursor=conn.cursor()
with open ('products.csv','r',encoding='utf-8')as file:
    reader=csv.DictReader(file)
    rows=[(
        int(row['id']),
        float(row['cost']),
        row['category'],
        row['name'],
        row['brand'],
        float(row['retail_price']),
        row['department'],
        row['sku'],
        int(row['distribution_center_id'])
    ) for row in reader
    ]
    cursor.executemany('''
    INSERT INTO products (id, cost, category, name, brand, retail_price, department, sku, distribution_center_id)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', rows)
conn.commit()
conn.close()