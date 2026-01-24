from flask import Flask, jsonify, request

app = Flask(__name__)

# Intial items in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]

@app.route('/')
def home():
    return "Welcome to the sample to do list."


# Get: retieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# Retrieve a specify item with by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"})
    return jsonify(item)


# Create a new Item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "invalid request"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item)


# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)


# Delete an item with by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"})
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "item deleted"})


if __name__ == '__main__':
    app.run(debug=True)
