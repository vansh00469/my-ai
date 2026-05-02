from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

bot = pipeline("text-generation", model="distilgpt2")

conversation = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation
    
    msg = request.json["message"]
    conversation += "User: " + msg + "\nAI:"

    res = bot(conversation, max_length=80)
    reply = res[0]["generated_text"].split("AI:")[-1]

    conversation += reply + "\n"

    return jsonify({"reply": reply.strip()})


   if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
