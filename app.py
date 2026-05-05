from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

paid_users = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user = data.get("user")
    msg = data.get("message")

    if user not in paid_users:
        return jsonify({"reply": "Please pay ₹50 to use AI."})

    reply = "🤖 AI: You said -> " + msg

    return jsonify({"reply": reply})

@app.route("/payment-success", methods=["POST"])
def payment_success():
    data = request.json
    user = data.get("user")

    paid_users[user] = True
    return jsonify({"status": "unlocked"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
