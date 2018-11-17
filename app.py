from flask import Flask, redirect,request, make_response, url_for, render_template
from learnflask.forms import LoginForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
import click
app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
bootstrap.init_app(app)
db.init_app(app)
from learnflask.models import User
app.secret_key=('fdasdfasd')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///' + os.path.join(app.root_path,'data.db'))

@app.route('/')
def showbooks():
    return render_template('books.html')

@app.route('/base')
def basetmp():
    return render_template('base.html')

@app.route('/child')
def childtmp():
    return render_template('child.html')

def inject_feng():
    feng = {'name':'feng',}
    return dict(feng=feng)
app.context_processor(inject_feng)

@app.route('/form',methods=['GET','POST'])
def formtest():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
    return render_template('form.html',form=form)

@app.cli.command()
def initdb():
    db.drop_all()
    db.create_all()
    click.echo(' Initialized database.')
    #可以在命令行下输入 flask initdb即可创建数据库和表


