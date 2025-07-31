from flask import Flask, jsonify, abort, request
import sqlite3

app = Flask(__name__)

DATABASE = 'ecommerce.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Not found', 'message': error.description if hasattr(error, 'description') else 'Resource not found'})
    response.status_code = 404
    return response

@app.errorhandler(400)
def bad_request(error):
    response = jsonify({'error': 'Bad request', 'message': error.description if hasattr(error, 'description') else 'Invalid request'})
    response.status_code = 400
    return response

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    products_list = [dict(product) for product in products]
    return jsonify(products_list), 200

@app.route('/api/products/<product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product_id_int = int(product_id)
    except ValueError:
        abort(400, description="Product ID must be an integer")
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (product_id_int,)).fetchone()
    conn.close()
    if product is None:
        abort(404, description="Product not found")
    return jsonify(dict(product)), 200

if __name__ == '__main__':
    app.run(debug=True)
