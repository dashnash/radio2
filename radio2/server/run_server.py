'''
Created on Jan 24, 2015

@author: dnash
'''

from flask import Flask

app = Flask("radio2")
app.debug = True

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run()