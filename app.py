from flask import Flask,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

from flask_sqlalchemy import SQLAlchemy # temporary database for storing information
from datetime import datetime

posts=[

    {
        'Author' : 'Anoop',
        'Title' : 'Blog post 1',
        'Content' : '1st post',
        'Date' : '20th Jan 2023'
    },
    {
        'Author' : 'Ananya',
        'Title' : 'Blog post 2',
        'Content' : '2nd post',
        'Date' : '30th Jan 2023'
    },
    {
        'Author' : 'Sreekala',
        'Title' : 'Blog post 3',
        'Content' : '3rd post',
        'Date' : '23th Jan 2023'
    },
    {
        'Author' : 'Johny',
        'Title' : 'Blog post 4',
        'Content' : '4th post',
        'Date' : '23th Jan 2023'
    }

]
app = Flask(__name__)

# the configuration variables are usually defined as uppercase strings.
# This is a convention to help distinguish them from other variables in the code.

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# 3 slashes for the relative path to the place where u want the db to be created

db=SQLAlchemy(app)

with app.app_context():
    db.create_all()
#C:\Users\anoop\PycharmProjects\FlaskBlog
import sqlite3

class User(db.Model):  # user model

    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(20), unique=True, nullable = False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    image_file = db.Column(db.String(20), nullable = False, default='default.jpeg')

    password = db.Column(db.String(60), nullable = False)

    posts = db.relationship('Post', backref = 'author', lazy=True) # posts has relationship to the post model
    #backref adds a another column to the posts
    #lazy just defines when sqlalchemy loads the data from the database
    def __repr__(self):    # dunder repr to give back string
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):  # posts model from user

    id = db.Column(db.Integer, primary_key = True)

    title = db.Column(db.String(100), nullable = False)

    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)  # we use utcnow instead of utcnow() to pass the time func to database instead

    content = db.Column(db.Text, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):  # dunder repr to give back string
        return f"Post('{self.title}','{self.date_posted}')"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !','success')
        redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in! 🥳','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check Username and password 😶😕','danger')
    return render_template('login.html', title='Login', form=form)


if __name__=="__main__":
    app.run(debug=True)