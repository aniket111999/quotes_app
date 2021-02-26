from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hbitlfxeslvlzw:3d9d3541d6ce14aa6098cc0d7285595c3030cc533f56c5d1c889e4ef6e28f7bc@ec2-18-207-95-219.compute-1.amazonaws.com:5432/dakc7f00e2uar3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Favqoutes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favqoutes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/process',methods=['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favqoutes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
