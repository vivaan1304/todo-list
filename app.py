from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask import render_template

app = Flask(__name__) # creates the flask app
app.config['SECRET_KEY'] = 'anything' # to generate csrf token
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # set URI for database can change sqlite to something else as wells

db = SQLAlchemy(app) # create database

from routes import * # import everything from routes.py, dont add before line 4 as app is needed in routes.py


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
