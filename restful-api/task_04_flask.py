from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    # Returns a list of all keys (usernames) from the dictionary
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # 1. Parse JSON data
    data = request.get_json()
    
    # Handle invalid JSON
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    # 2. Extract username
    username = data.get("username")
    
    # 3. Validation
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # 4. Save user and return success
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
