# -----------------------------------------------------------------------------
# run.py
# Created by Ingrid Avendano 12/19/13.
# -----------------------------------------------------------------------------
# Contols different views and runs model depending on the view.
# -----------------------------------------------------------------------------

import os
from flask import Flask, render_template, request
import model

# -----------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = "heygurlhey"

# -----------------------------------------------------------------------------

app.route("/", methods=["GET"])
def index():
	return render_template("index.html")


app.route("/resume", methods=["GET"])
def resume():
	return render_template("resume.html")