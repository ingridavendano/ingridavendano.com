# -----------------------------------------------------------------------------
# controller.py
# Created by Ingrid Avendano 12/19/13.
# -----------------------------------------------------------------------------
# Contols different views and runs model depending on the view.
# -----------------------------------------------------------------------------

import os
from flask import Flask, render_template, request

# -----------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = "heygurlhey"

# -----------------------------------------------------------------------------

@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


@app.route("/resume", methods=["GET"])
def resume():
	return render_template("resume.html")

# -----------------------------------------------------------------------------

if __name__ == "__main__":

	port = int(os.getenv('CIRCUIT_PORT', 5000))
	app.run(host='0.0.0.0', port=port)
