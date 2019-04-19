from os import name
from sqlalchemy import desc,select
from flask_msearch import Search
from flask import Flask, render_template, request,session,redirect,session
from  flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from jieba.analyse import ChineseAnalyzer
from flask_wtf import FlaskForm


app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] =  "mysql://root:@localhost/tag"



db = SQLAlchemy(app)

class AHMEDABAD(db.Model):
    __tablename__ = 'ahmedabad'
    __searchable__ = ['school_name','location','address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255),nullable=False)
    location = db.Column(db.String(50),nullable=False)
    address= db.Column(db.String(50),nullable=False)

class RAJKOT(db.Model):
    __tablename__ = 'rajkot'
    __searchable__ = ['school_name','location','address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255),nullable=False)
    location = db.Column(db.String(50),nullable=False)
    address= db.Column(db.String(50),nullable=False)

class ANAND(db.Model):
    __tablename__ = 'anand'
    __searchable__ = ['school_name','location','address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255),nullable=False)
    location = db.Column(db.String(50),nullable=False)
    address= db.Column(db.String(50),nullable=False)

class JAMNAGAR(db.Model):
    __tablename__ = 'jamnagar'
    __searchable__ = ['school_name','location','address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255),nullable=False)
    location = db.Column(db.String(50),nullable=False)
    address= db.Column(db.String(50),nullable=False)

class GANDHINAGAR(db.Model):
    __tablename__ = 'gandhinagar'
    __searchable__ = ['school_name','location','address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255),nullable=False)
    location = db.Column(db.String(50),nullable=False)
    address= db.Column(db.String(50),nullable=False)

class BARODA(db.Model):
    __tablename__ = 'baroda'
    __searchable__ = ['school_name', 'location', 'address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)

class VADODRA(db.Model):
    __tablename__ = 'vadodra'
    __searchable__ = ['school_name', 'location', 'address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)

class MEHSANA(db.Model):
    __tablename__ = 'mehsana'
    __searchable__ = ['school_name', 'location', 'address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)

class SURAT(db.Model):
    __tablename__ = 'surat'
    __searchable__ = ['school_name', 'location', 'address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)

class NEW(db.Model):
    __tablename__ = ''
    __searchable__ = ['school_name', 'location', 'address']
    __msearch_analyzer__ = ChineseAnalyzer()
    sno = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)

search = Search()
search.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/city/<string:location>')
def city(location):
    if location=='ahmedabad':
        final= AHMEDABAD.query.all()
        new="ahmedabad"
    elif location == "anand":
        final= ANAND.query.all()
        new = "anand"
    elif location == "rajkot":
        final= RAJKOT.query.all()
        new = "rajkot"
    elif location == "mehsana":
        final= MEHSANA.query.all()
        new = "mehsana"
    elif location == "vadodra":
        final= VADODRA.query.all()
        new = "vadodra"
    elif location == "surat":
        final= SURAT.query.all()
        new = "surat"
    elif location == "baroda":
        final= BARODA.query.all()
        new = "baroda"
    elif location == "jamnagar":
        final= JAMNAGAR.query.all()
        new = "jamnagar"
    elif location == "gandhinagar":
        final= GANDHINAGAR.query.all()
        new = "gandhinagar"
    return render_template('tabl.html',final=final,new=new)



@app.route('/dashboard' , methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        school_name = request.form.get('school_name')
        location = request.form.get('location')
        address = request.form.get('address')
        if location=="gandhinagar":
            gandhinagar = GANDHINAGAR(school_name=school_name, location=location, address=address)
            db.session.add(gandhinagar)
            db.session.commit()
        elif location=="rajkot":
            rajkot = RAJKOT(school_name=school_name, location=location,address=address)
            db.session.add(rajkot)
            db.session.commit()
        elif location == "anand":
            anand = ANAND(school_name=school_name, location=location, address=address)
            db.session.add(anand)
            db.session.commit()
        elif location == "surat":
            surat = SURAT(school_name=school_name, location=location, address=address)
            db.session.add(surat)
            db.session.commit()
        elif location == "mehsana":
            mehsana = MEHSANA(school_name=school_name, location=location, address=address)
            db.session.add(mehsana)
            db.session.commit()
        elif location == "vadodra":
            vadodra = VADODRA(school_name=school_name, location=location, address=address)
            db.session.add(vadodra)
            db.session.commit()
        elif location == "ahmedabad":
            ahmedabad = AHMEDABAD(school_name=school_name, location=location, address=address)
            db.session.add(ahmedabad)
            db.session.commit()
        elif location == "baroda":
            baroda = BARODA(school_name=school_name, location=location, address=address)
            db.session.add(baroda)
            db.session.commit()
        elif location == "jamnagar":
            jamnagar = JAMNAGAR(school_name=school_name, location=location, address=address)
            db.session.add(jamnagar)
            db.session.commit()
    return render_template('fill.html')

@app.route("/search/<string:location>/",methods=['GET','post'])
def search(location):
        if location == "ahmedabad" :
            final =AHMEDABAD.query.msearch(request.args.get('query')).all()
            new="ahmedabad"
        elif location == "anand":
            final = ANAND.query.msearch(request.args.get('query')).all()
            new = "anand"
        elif location == "rajkot":
            final = RAJKOT.query.msearch(request.args.get('query')).all()
            new = "rajkot"
        elif location == "mehsana":
            final = MEHSANA.query.msearch(request.args.get('query')).all()
            new = "mehsana"
        elif location == "vadodra":
            final = VADODRA.query.msearch(request.args.get('query')).all()
            new = "vadodra"
        elif location == "surat":
            final = SURAT.query.msearch(request.args.get('query')).all()
            new = "surat"
        elif location == "baroda":
            final = BARODA.query.msearch(request.args.get('query')).all()
            new = "baroda"
        elif location == "jamnagar":
            final = JAMNAGAR.query.msearch(request.args.get('query')).all()
            new = "jamnagar"
        elif location == "gandhinagar":
            final = GANDHINAGAR.query.msearch(request.args.get('query')).all()
            new = "gandhinagar"
        return render_template('tabl.html', final=final,new=new)


app.run(debug=True)