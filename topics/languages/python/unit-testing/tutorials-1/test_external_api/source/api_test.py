from flask import Flask
from flask import jsonify, request


app = Flask(__name__)

# Simulated database (in-memory)
# Consider this as a data source
users = {}


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return user info by ID."""
    user = users.get(user_id, None)
    if user:
        return jsonify({"id": user_id, "name": user}), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def add_user():
    """Adds a new users."""
    # convert JSON response into python dict
    data = request.json
    user_id = data.get('id')
    name = data.get('name')

    if not user_id or not name:
        return jsonify({"error": "Invalid data"}), 404
