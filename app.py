from flask import Flask, render_template, request, jsonify 
import requests, random
# from validate import Validate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "lucky"

@app.route("/")
def homepage():
    """Show homepage."""

    
    return render_template("index.html")




@app.route("/api/get-lucky-num", methods=["POST"])
def lucky_num():
    
    random_num = random.randint(1,100)
    # colors = ["red", "green", "orange", "blue"]
    errors = {"error": {}}
    valid_colors = "red", "blue", "green", "orange"
    name = request.json["name"]
    year = request.json["year"]
    color = request.json["color"]
    email = request.json["email"]

    if email not in request.json or request.json["email"] is "":
        errors["error"]["email"] = "Email is required"
    if name not in request.json or request.json["name"] is "":
        errors["error"]["name"] = "Name is required."
    if year not in request.json or request.json["year"] is "":
        errors["error"]["year"] = "Year is required."
    elif int(request.json["year"]) < 1900 or int(request.json["year"])> 2000:
        errors["error"]["year"] = "Year must be between 1900 and 2000, inclusive."
    if color not in request.json or request.json["color"] is "":
        errors["error"]["color"] = "Color is required."
    elif request.json["color"].lower() not in valid_colors:
        errors["error"]["color"] = "Invalid color."

    if len(errors["error"]) != 0:
        res_obj = errors
        res_json = jsonify(res_obj)
        return res_json

    else:
        random_fact = requests.get(f'http://numbersapi.com/{random_num}/trivia')
        input_year = requests.get(f'http://numbersapi.com/{year}/year')

        res_obj = {"num" : {"fact" : random_fact.text, "num" : random_num},
                           "year" : {"fact" : input_year.text, "year" : year }
                          }
        res_json = jsonify(res_obj)
        return res_json



