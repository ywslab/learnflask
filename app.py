from flask import Flask, redirect,request, make_response, url_for, render_template


app = Flask(__name__)

user = {
    'username': 'feng',
    'bio': 'this guy are lazy,nothing left',
}
books = [{'name': 'computer', 'year': 1998},
         {'name': 'caozuoxitong', 'year': 2008},
         {'name': 'jisuanjiwangluo', 'year': 2010},]


@app.route('/')
def showbooks():
    return render_template('books.html', books=books, user=user)

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
