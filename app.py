from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=covergirl&product_type=foundation"
    response = requests.get(url)
    dados = response.json()

    return render_template("index.html", teste=dados)


if __name__ == '__main__':
    app.run()
