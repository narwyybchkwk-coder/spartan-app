from flask import Flask, request, jsonify

app = Flask(__name__)

messages = [{"user":"کاربر ۱","text":"سلام!"}]

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

@app.route("/messages", methods=["POST"])
def add_message():
    data = request.get_json()
    text = data.get("text", "").strip()
    if text:
        messages.append(text)
    return jsonify({"ok": True})

app.run(host="0.0.0.0", port=5000)
