from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = '9);}%N>Y&KIj,oc'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bio', methods=['GET', 'POST'])
def bio():
    # GET and POST requests both render the bio page for now
    if request.method in ['GET', 'POST']:
        return render_template('bio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # GET and POST requests both render the contact page for now
    if request.method in ['GET', 'POST']:
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
    return render_template('signup.html')

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
    
    