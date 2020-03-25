from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
 
app = Flask(__name__)
 
bot = ChatBot(
    'С˼',
    database_uri='sqlite:///db.sqlite3'
)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

@app.route("/api/chat/<text>")
def get_bot_api(text):
    res = str(bot.get_response(text))
    return jsonify(res), 200


if __name__ == "__main__":
	app.run(host='0.0.0.0')