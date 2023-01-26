from flask import Flask,render_template, url_for

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__=="__main__":
    app.run(debug=True)