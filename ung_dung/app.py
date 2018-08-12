from ung_dung import app

@app.route('/')
def index():
    return '<h1>Make some noise.</h1>'