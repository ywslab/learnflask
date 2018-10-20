# -*- coding:utf-8 -*-
from flask import Flask

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
