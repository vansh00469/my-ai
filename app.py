from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

user_count = {}

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_ip = request.remote_addr

        if user_ip not in user_count:
            user_count[user_ip] = 0

        if user_count[user_ip] >= 5:
            return jsonify({"reply": "Limit reached. Pay ₹50 to continue."})

        user_count[user_ip] += 1

        msg = request.json.get("message")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": msg}]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})
    app.run(host="0.0.0.0", port=10000)
