"""Server for project web app."""

from flask import (Flask, render_template)

from jinja2 import StrictUndefined

app = Flask(__name__, template_folder='./src')
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

@app.errorhandler(404)
def not_found(_error):
    return render_template("index.html")

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=5001)