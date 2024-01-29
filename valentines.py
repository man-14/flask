from flask import Flask, render_template;

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/SHE_SAID_YESSSS")
def SHE_SAID_YESSSS():
	return render_template("yes.html")

@app.route("/message_hehe")
def message_hehe():
	return render_template("message.html")

if __name__ == "__main__":
	app.run(debug=True)