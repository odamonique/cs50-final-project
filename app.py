from flask import Flask, render_template, request, session
import os
from flask_session import Session

#Configure app
app = Flask(__name__)

#Configure session
app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

images=os.path.join("static", "images")
app.config["UPLOAD_FOLDER"]= images
chocolate_Images = os.listdir("static/images/chocolates")
print(len(chocolate_Images))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/favorites", methods=["GET", "POST"])
def favorites():
    #Ensure favorites exist
    if "favourite" not in session:
        session["favourite"]= {}

    if request.method == "POST":
        
        image_path = request.form.get("id")
        favorite_dic = session["favourite"]
        if image_path not in favorite_dic:
            favorite_dic[image_path] = image_path
 
        print(favorite_dic)

        return render_template("favorites.html")
    
    return render_template("favorites.html")

@app.route("/pricelist")
def pricelist():
    return render_template("/pricelist.html")

@app.route("/chocolates")
def chocolates():

    # chocolate_images = os.listdir("static/images/chocolates")
    chocolate_images = ["images/chocolates/" + images for images in chocolate_Images] 
    # len_chocolates = len(chocolate_images)
    # chocolate = {}
    # for k,v in enumerate(chocolate_images):
    #     key = k
    #     image = v
    #     chocolate[key] = image
 
    return render_template("/chocolates.html", chocolate=chocolate_images)

@app.route("/decorations")
def decorations():
    return render_template("/decorations.html")

@app.route("/gifts")
def gifts():
    return render_template("/gifts.html")