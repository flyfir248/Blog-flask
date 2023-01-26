from flask import Flask,render_template, url_for
from forms import RegistrationForm, LoginForm

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

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__=="__main__":
    app.run(debug=True)