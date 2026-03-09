"""
Simple Flask application for testing graph ingestion.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
print("huyguy")
# In-memory data store
users = [
    {"id": 600, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

print("hello")
@app.route("/api/users", methods=["GET"])
def get_users():
    """Return all users."""
    return jsonify(users)


@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Return a single user by ID."""
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/api/users", methods=["POST"])
def create_user():
    """Create a new user."""
    data = request.get_json()
    new_user = {
        "id": max(u["id"] for u in users) + 1,
        "name": data["name"],
        "email": data["email"],
    }
    users.append(new_user)
    return jsonify(new_user), 201


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
