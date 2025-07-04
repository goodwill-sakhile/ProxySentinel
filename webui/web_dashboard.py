from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Web Filter Dashboard</h1>"

@app.route("/rules", methods=["GET"])
def get_rules():
    return jsonify({"rules": "List of rules here"})

if __name__ == "__main__":
    app.run(port=5000)
