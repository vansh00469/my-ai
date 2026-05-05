from flask import Flask, request, jsonify, render_template
import random
import json

app = Flask(__name__)

# 🔐 Load paid users (persistent)
try:
    with open("paid.json", "r") as f:
        paid_users = json.load(f)
except:
    paid_users = {}

def save_users():
    with open("paid.json", "w") as f:
        json.dump(paid_users, f)

@app.route("/")
def home():
    return render_template("index.html")

# 🧠 SMART FAKE AI
def fake_ai_reply(msg):
    msg = msg.lower()

    # greetings
    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "Hey! Nice to see you 😄"

    # name
    if "your name" in msg:
        return "You can call me Nova 🤖"

    # jokes
    if "joke" in msg:
        jokes = [
            "Why don’t programmers like nature? Too many bugs 🐛😂",
            "Why did the computer catch a cold? Because it left its Windows open 🤧💻",
            "I told my AI a joke… it crashed 🤖💀😂"
        ]
        return random.choice(jokes)

    # how are you
    if "how are you" in msg:
        return "I'm doing great 😄 thanks for asking!"

    # explain
    if "explain" in msg:
        return "Sure 😄 tell me what you want me to explain!"

    # question type
    if any(word in msg for word in ["what", "why", "how"]):
        return "Hmm 🤔 that's a good question. Let me think..."

    # default replies
    return random.choice([
        "Interesting 👀 tell me more",
        "I understand 🙂",
        "That sounds cool 😎",
        "Can you explain more?"
    ])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user = data.get("user")
    msg = data.get("message")

    # 🔒 lock if not paid
    if not paid_users.get(user):
        return jsonify({"reply": "Please pay ₹50 to unlock AI 🔒"})

    reply = fake_ai_reply(msg)
    return jsonify({"reply": reply})

@app.route("/payment-success", methods=["POST"])
def payment_success():
    data = request.json
    user = data.get("user")

    paid_users[user] = True
    save_users()

    return jsonify({"status": "unlocked"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
