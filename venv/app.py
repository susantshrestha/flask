
from flask import Flask, render_template, request, url_for,redirect, session,flash
from functools import wraps


#  create the application object
app = Flask(__name__)

app.secret_key= "my precious"

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorator to link the function to a url
@app.route('/')
@login_required
def home():
    return render_template('index.html')
    # return 'hello world'

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid credential. please try again'
        else:
            session['logged_in']=True
            flash('you are logged in!')
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in',None)
    flash('you are just logged out!')
    return redirect(url_for('welcome'))

# start the server with the 'run()' method
if __name__=='__main__':
    app.run(debug=True)



