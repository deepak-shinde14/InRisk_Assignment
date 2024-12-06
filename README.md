Flask REST API: Product Management
This project is a simple REST API built with Flask that fetches, stores, and manipulates product data using an external open-source API. The API allows clients to view and add products, with data stored in memory during runtime.

Features
GET /products:

Fetches and returns a list of products.
Uses the Dummy JSON API (https://dummyjson.com/products) to populate the initial product list.
POST /products:

Accepts a new product in JSON format and temporarily adds it to the product list.
Validates the incoming data to ensure it includes title, price, and category.
Error Handling:

Gracefully handles:
Validation errors for POST requests.
External API errors (e.g., API unreachable).
Other unexpected errors.

API Endpoints
1. GET /products
Description: Fetches the list of products.
Response:
json
Copy code
[
  {
    "id": 1,
    "title": "Sample Product",
    "price": 19.99,
    "category": "electronics"
  },
  ...
]
2. POST /products
Description: Adds a new product to the list.

Request Body:

json
Copy code
{
  "title": "Sample Product",
  "price": 19.99,
  "category": "electronics"
}
Validation:

title: Required (non-empty string).
price: Required (number).
category: Required (non-empty string).
Response:

Success (201):
json
Copy code
[
  {
    "id": 1,
    "title": "Sample Product",
    "price": 19.99,
    "category": "electronics"
  },
  {
    "id": 2,
    "title": "New Product",
    "price": 25.99,
    "category": "books"
  }
]
Validation Error (400):
json
Copy code
{
  "error": "Invalid data. 'title', 'price', and 'category' are required."
}
Error Handling
404 Not Found: Resource not found.
400 Bad Request: Invalid POST data.
500 Internal Server Error: Unexpected server issues.
503 Service Unavailable: External API unreachable.
