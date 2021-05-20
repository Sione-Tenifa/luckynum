from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


# import requests



# resp = requests.get(
#     'http://numbersapi.com/random/year')

# print(resp.json())



# x = requests.get('https://w3schools.com')
# print(x.status_code)