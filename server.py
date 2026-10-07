from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)
messages = [{"user": "کاربر ۱", "text": "سلام!"}]

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

@app.route("/messages", methods=["POST"])
def add_message():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if text:
        messages.append({"user": "کاربر", "text": text})
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
