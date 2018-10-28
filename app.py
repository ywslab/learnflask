# -*- coding:utf-8 -*-
from flask import request,make_response,url_for
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello,is me</h1>"

#绑定多个url
@app.route('/fengguifan')
@app.route('/fengxuezhang')
def fengguifan():
    return "<h1>Hello,i am fengguifan</h1>"

#动态url
#为设置默认参数
@app.route('/greet',defaults={'name':'fengguifan'})
@app.route('/greet/<name>')
def greet(name):
    return "<h1>Hello,%s!</h1>" % name

#获取查询字符串
#使用示例/hello?name=feng
#需要注意的是，这里存在安全漏洞
@app.route('/hello',methods=['GET','POST'])
def hello():
    name = request.args.get('name','Flask')
    return "<h1>hello,%s!</h1>"  % name

#url变量转换器
@app.route('/goto/<int:year>')
def goto(year):
    return '<h1>Welcome to %s!<h1>' % year

@app.route('/colors/<any(blue,white,red):color>')
def three_colors(color):
    return '<h1>color %s </h1> ' %color
#Hook
'''
@app.before_request
def do_something():
    return '<h1>hahahhahaha</h1>'
'''
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hi')))
    response.set_cookie('name',name)
    return response

@app.route('/hi')
def hi():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','Human')
    return '<h1>Hello,%s</h1>' %name
