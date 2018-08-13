from ung_dung import app
from flask import Flask, render_template

@app.route('/test')
def test():
    return render_template('mh.html')