from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)

# Define the Item model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database tables (run this once)
# with app.app_context():
#    db.create_all()

# Sample data to store items
# Remove this as we will now use the database
# items = []

@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    items_data = [{'id': item.id, 'name': item.name} for item in items]
    return jsonify({'items': items_data})

# Modify other routes to use the database (POST, PUT, DELETE)
# ...
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'Name is required'}), 400

    new_item = Item(name=data['name'])
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify({'id': new_item.id, 'name': new_item.name}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404

    item.name = data['name']
    db.session.commit()

    return jsonify({'id': item.id, 'name': item.name})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({'message': 'Item deleted'})

if __name__ == '__main__':
    app.run(debug=True)