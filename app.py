from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder="template", static_url_path='/static')

@app.route('/')
def home():
    return render_template("index.html")
  
products = {
    '101': {'id': '101', 'name': 'Product 1', 'price': 10.00},
    '102': {'id': '102', 'name': 'Product 2', 'price': 20.00},
    '103': {'id': '103', 'name': 'Product 3', 'price': 15.00}
}

@app.route('/get-product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4450))
    app.run(host='0.0.0.0', port=port, debug=True)
