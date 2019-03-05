from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    products = requests.get('http://product-service').json().get('products')
    return render_template('home.html', products=products)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=90, debug=True)
