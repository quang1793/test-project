from flask import Flask
app=Flask(__name__)

app.config['SECRET_KEY'] = '123456790'
import ung_dung._app