"""Server for personal portfolio."""

from flask import (Flask, render_template)

from jinja2 import StrictUndefined

app = Flask(__name__, template_folder='./src')
# app.secret_key = "dev"
# app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=5001)