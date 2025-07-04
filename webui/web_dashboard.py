from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Web Filter Dashboard</h1>"

@app.route("/rules", methods=["GET"])
def get_rules():
    return jsonify({"rules": "List of rules here"})
from flask import Flask, jsonify, request

app = Flask(__name__)

rules = {
    "blocked_ips": ["192.168.1.10"],
    "blocked_keywords": ["adult"],
    "blocked_domains": ["badwebsite.com"]
}

@app.route("/")
def index():
    return "<h1>Python Web Filter Admin Dashboard</h1>"

@app.route("/api/rules", methods=["GET", "POST"])
def manage_rules():
    if request.method == "GET":
        return jsonify(rules)
    elif request.method == "POST":
        data = request.json
        rules.update(data)
        return jsonify({"status": "Rules updated", "rules": rules})

@app.route("/api/status")
def status():
    return jsonify({"status": "Proxy server is running."})

if __name__ == "__main__":
    app.run(port=5000, debug=True)


if __name__ == "__main__":
    app.run(port=5000)
