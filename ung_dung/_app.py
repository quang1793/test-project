from ung_dung import app
from flask import Flask

@app.route('/')
def index():
    return '<h1>Make some noise.</h1>'