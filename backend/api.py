from flask import Flask, jsonify, abort
import sqlite3

app = Flask(__name__)

DATABASE = 'ecommerce.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    products_list = [dict(product) for product in products]
    return jsonify(products_list), 200

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id,)).fetchone()
    conn.close()
    if product is None:
        abort(404, description="Product not found")
    return jsonify(dict(product)), 200

if __name__ == '__main__':
    app.run(debug=True)
