from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

paid_users = {}

@app.route("/")
def home():
    return render_template("index.html")

# 🧠 FAKE AI BRAIN
def fake_ai_reply(msg):
    msg = msg.lower()

    if "hi" in msg or "hello" in msg:
        return random.choice([
            "Hey there! 😊",
            "Hello! How can I help you?",
            "Hi! What's up?",
            "Hey! Nice to see you 😄"
        ])

    elif "name" in msg:
        return "I'm your personal AI assistant 🤖"

    elif "how are you" in msg:
        return random.choice([
            "I'm doing great! 😄",
            "All good! What about you?",
            "Feeling smart today 😎"
        ])

    elif "bye" in msg:
        return "Goodbye! Come back soon 👋"

    elif "what" in msg or "why" in msg or "how" in msg:
        return "That's an interesting question 🤔 Let me think... I believe it's because things work that way in most cases."

    else:
        return random.choice([
            "Hmm... tell me more 🤔",
            "Interesting... continue 👀",
            "I understand 🙂",
            "Can you explain more?",
            "That sounds cool 😎"
        ])

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user = data.get("user")
    msg = data.get("message")

    # 🔒 lock if not paid
    if user not in paid_users:
        return jsonify({"reply": "Please pay ₹50 to unlock AI 🔒"})

    reply = fake_ai_reply(msg)
    return jsonify({"reply": reply})

@app.route("/payment-success", methods=["POST"])
def payment_success():
    data = request.json
    user = data.get("user")

    paid_users[user] = True
    return jsonify({"status": "unlocked"})

if __name__ == "__main__":
    app.run()
