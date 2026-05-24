### PUT and DELETE - HTTP Verbs
### Working with APIs -- JSON

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initial data in todo list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
    {"id": 3, "name": "Item 3", "description": "This is item 3"},
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Todo List App"

# GET: Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({"message": "Item not found"}), 404
    else:
        return jsonify(item)

# POST: Create a new item
@app.route('/items', methods=['POST'])
def create_item():

    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }

    items.append(new_item)

    return jsonify(new_item), 201

# PUT: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):

    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get(
        'description',
        item['description']
    )

    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):

    global items  #it helps to modify the global variable``

    item = next((item for item in items if item['id'] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    items = [item for item in items if item['id'] != item_id]

    return jsonify({"message": "Item deleted successfully"})

# Run app
if __name__ == '__main__':
    app.run(debug=True)

