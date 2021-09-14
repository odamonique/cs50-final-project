from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pricelist")
def pricelist():
    return render_template("/pricelist.html")

@app.route("/chocolates")
def chocolates():
    return render_template("/chocolates.html")

@app.route("/decorations")
def decorations():
    return render_template("/decorations.html")

@app.route("/gifts")
def gifts():
    return render_template("/gifts.html")