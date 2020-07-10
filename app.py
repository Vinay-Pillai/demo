from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = '9);}%N>Y&KIj,oc'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bio', methods=['GET', 'POST'])
def bio():
    # GET and POST requests both render the bio page for now
    if request.method == 'POST':
        # Once the backend is setup the code below should change
        return request.args
    else:
        return render_template('bio.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # GET and POST requests both render the contact page for now
    if request.method == 'POST':
        return request.args
    else:
        return render_template('contact.html')

@app.route('/stories', methods=['GET', 'POST'])
def stories():
    if request.method == 'POST':
        return request.args
    else:
        return render_template('stories.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'Chiguru' and password == 'lemon':
            session['logged_in'] = True
            return redirect(url_for('home'))

        return render_template('login.html')

    else:
        # TODO Check signup form data and edit session variable
        pass
    return render_template('login.html')

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
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return 'Nothing Here Yet\n Add about.html and render it in the app.py'

@app.errorhandler(404)
def error_not_found_404(error):
    print(error)
    return 'Page Not found'

if __name__ == "__main__":
    app.debug = True
    app.run()