from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Store the product list in memory
products = []

# Function to fetch initial products
def fetch_initial_products():
    global products
    try:
        response = requests.get("https://dummyjson.com/products")
        response.raise_for_status()
        products = response.json().get("products", [])
    except requests.RequestException:
        app.logger.error("Failed to fetch data from the Dummy JSON API.")
        products = []

# Populate the products list when the app starts
fetch_initial_products()

@app.route('/products', methods=['GET', 'POST'])
def handle_products():
    global products

    if request.method == 'GET':
        return jsonify(products)

    if request.method == 'POST':
        # Validate and process the POST request
        data = request.get_json()
        if not data or not all(data.get(key) for key in ['title', 'price', 'category']):
            return jsonify({"error": "Invalid data. 'title', 'price', and 'category' are required."}), 400

        # Create and append a new product
        new_product = {
            "id": len(products) + 1,
            "title": data["title"],
            "price": data["price"],
            "category": data["category"]
        }
        products.append(new_product)
        return jsonify(products), 201

# Global error handler
@app.errorhandler(Exception)
def handle_exception(error):
    error_message = getattr(error, 'description', str(error))
    status_code = getattr(error, 'code', 500)
    return jsonify({"error": error_message}), status_code

if __name__ == '__main__':
    app.run(debug=True)
