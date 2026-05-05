from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="YOUR_API_KEY_HERE")

paid_users = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user = data.get("user")

    # 🔒 block if not paid
    if user not in paid_users:
        return jsonify({"reply": "Please pay ₹50 to use AI."})

    msg = data.get("message")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": msg}]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})

@app.route("/payment-success", methods=["POST"])
def payment_success():
    data = request.json
    user = data.get("user")

    paid_users[user] = True
    return jsonify({"status": "unlocked"})

if __name__ == "__main__":
    app.run()
