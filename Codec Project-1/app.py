from flask import Flask, render_template
from speech import SpeechToText

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/record")
def record():

    stt = SpeechToText()

    result = stt.record_audio()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)