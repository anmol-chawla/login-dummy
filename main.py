from flask import Flask, request, render_template, jsonify
from charts.app import index

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['email']
    password  = request.form['password']
    text += " "
    text += password
    return index()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)