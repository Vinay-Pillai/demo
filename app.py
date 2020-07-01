from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')
    