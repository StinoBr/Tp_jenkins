from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur l'API de test du pipeline!"

@app.route("/echo", methods=["POST"])
def echo():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    data = request.get_json()
    message = data.get("message", "")
    return jsonify({"echo": message}), 200

if __name__ == "__main__":
    app.run(debug=True)
