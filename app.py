from IPython.display import YouTubeVideo
from IPython.display import display
from IPython.display import HTML
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    user1 = request.form.get("name")
    
    return render_template("index.html", video = user1)

if __name__ == "__main__":
	app.run(debug=True)