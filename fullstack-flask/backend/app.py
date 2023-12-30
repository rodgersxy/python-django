from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ



app = Flask(__name__)
CORS(app)  # enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return{'id': self.id, 'name': self.name, 'email': self.email}
db.create_all()

# create a test route
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'The server is running Successful'})

# create a user
@app.route('/api/flask/user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
    
        return jsonify({
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email
        }), 201
    except Exception as e:
        return make_response(jsonify({'message': 'An error occurred creating the user', 'error': str(e)}), 500)
    
# get all users
@app.route('/api/flask/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        user_data = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
        return jsonify(user_data), 200
    except Exception as e:
        return make_response(jsonify({'message': 'An error occurred getting the users', 'error': str(e)}), 500)

# get a user by id
@app.route('/api/flask/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'An error occurred getting the user', 'error': str(e)}), 500)

# update a user by id
@app.route('/api/flask/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'An error occurred updating the user', 'error': str(e)}), 500)
    
# delete a user by id
@app.route('/api/flask/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'User deleted'}), 200)
        return make_response(jsonify({'message': 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'An error occurred deleting the user', 'error': str(e)}), 500)