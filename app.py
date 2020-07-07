from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = b'\x10\x9aQsS\xe6T\xb6\x95M\x80X\xe3\xf3\t\xbc'

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'Chiguru' and password == 'lemon':
            session['logged_in'] = True
            return redirect(url_for('home.html'))

        return render_template('login.html')

    else:
        # TODO Check signup form data and edit session variable
        pass

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        # TODO Check signup form data and edit session variable
        pass

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login.html'))
    
    